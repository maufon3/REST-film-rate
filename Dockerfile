FROM python:3
ADD filmRate.py /
ADD key.txt /
RUN pip install requests
ENTRYPOINT [ "python", "./filmRate.py" ]
CMD []
