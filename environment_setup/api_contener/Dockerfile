FROM continuumio/miniconda3:latest
RUN mkdir -p /scripts
COPY workstation.sh /scripts
WORKDIR /scripts
RUN chmod +x workstation.sh
RUN ./workstation.sh
WORKDIR /usr/src/app
COPY . .
RUN pip install mlflow
RUN pip install flask
RUN pip install numpy
RUN pip install tensorflow==2.8.0
RUN conda install -c conda-forge mlflow
RUN conda install Pillow
WORKDIR /usr/src/app/api
CMD python app.py
