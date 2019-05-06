# use the official Nginx base image
FROM nginx:latest

ARG PROJECT_ROOT_FOLDER=chandassu
ARG PYTHON_VERSION=3.11

# set current working directory
WORKDIR /developer/projects/$PROJECT_ROOT_FOLDER
RUN echo "Current working directory: $(pwd)"

# install system package dependencies
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git lsof python$PYTHON_VERSION-dev

# install pyenv
RUN curl https://pyenv.run | bash

# install python and set that as default python version
RUN $HOME/.pyenv/bin/pyenv install --force $PYTHON_VERSION && \
    $HOME/.pyenv/bin/pyenv global $PYTHON_VERSION && \
    echo "Python version: $(python$PYTHON_VERSION --version)"

# install poetry
RUN curl -sSL https://install.python-poetry.org | python$PYTHON_VERSION -

# copy source code
COPY . .

# install project dependencies
RUN /root/.local/bin/poetry config virtualenvs.in-project true && \
    /root/.local/bin/poetry config virtualenvs.options.always-copy true && \
    /root/.local/bin/poetry config virtualenvs.path "venv" && \
    /root/.local/bin/poetry install

RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx_original.conf
RUN cp nginx.conf /etc/nginx/nginx.conf

# Expose the port on which Nginx will listen
EXPOSE 80

# Start (Nginx daemon service in the background) AND (uWSGI in the foreground to serve the Flask application)
CMD service nginx start && \
    . .venv/bin/activate && \
    uwsgi --ini uwsgi.ini
