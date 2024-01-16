print("Added This")

FROM openjdk:8-jre-slim

WORKDIR /usr/src/app

COPY . .

RUN javac SumOfDigits.java

CMD ["java", "SumOfDigits"]
