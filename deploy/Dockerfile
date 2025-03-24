#FROM public.ecr.aws/lambda/python:3.11
#
#COPY prediction_model.pkl .
#
#COPY requirements.txt  .
#RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
#
## Copy function code
#COPY app.py ${LAMBDA_TASK_ROOT}
#
#CMD [ "app.handler" ]


# Use AWS Lambda Python 3.11 base image
FROM public.ecr.aws/lambda/python:3.11

# Copy model file
COPY prediction_model.pkl ${LAMBDA_TASK_ROOT}/prediction_model.pkl

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy application code
COPY app.py ${LAMBDA_TASK_ROOT}/app.py

# Set the Lambda function handler
CMD [ "app.handler" ]
