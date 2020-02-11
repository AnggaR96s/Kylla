FROM anggarsx/arch:20200211
RUN mkdir /bot
RUN chmod 777 /bot
WORKDIR /bot
RUN git clone https://github.com/anggar96s/kylla /bot

CMD ["python3","-m","stdborg"]
