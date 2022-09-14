FROM python:3.9-alpine


RUN pip install textwrap3 svgwrite
RUN mkdir /app

WORKDIR /app

CMD python produce_svg.py


