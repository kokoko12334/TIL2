package org.example;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.logging.FileHandler;
import java.util.logging.SimpleFormatter;

public class Main {

    private static final Logger log4jLogger = LogManager.getLogger(Main.class);
    private static final org.slf4j.Logger logbackLogger = LoggerFactory.getLogger(Main.class);
    private static final java.util.logging.Logger julLogger = java.util.logging.Logger.getLogger(Main.class.getName());

    private static final int LOG_COUNT = 10; // 10만 개 로그

    public static void main(String[] args) throws IOException {
        System.out.println("Starting logging performance test...");

        // JUL (java.util.logging) 파일 핸들러 설정
        setupJulFileLogging();

        // JUL 설정 파일 적용
        try (InputStream configStream = Main.class.getClassLoader().getResourceAsStream("logging.properties")) {
            if (configStream != null) {
                java.util.logging.LogManager.getLogManager().readConfiguration(configStream);
            } else {
                System.err.println("Could not find logging.properties in classpath");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        double logbackSec = measurePerformance("Logback", () -> logbackLogger.info("Test log message"));
        double log4j2Sec = measurePerformance("Log4j 2", () -> log4jLogger.info("Test log message"));
//        double julSec = measurePerformance("java.util.logging (JUL)", () -> julLogger.info("Test log message"));

        System.out.printf("%s took: %.2f seconds%n", "Logback", logbackSec);
        System.out.printf("%s took: %.2f seconds%n", "Log4j 2", log4j2Sec);
//        System.out.printf("%s took: %.2f seconds%n", "java.util.logging (JUL)", julSec);
    }

    private static void setupJulFileLogging() throws IOException {
        FileHandler fileHandler = new FileHandler("logs/jul.log", true);
        fileHandler.setFormatter(new SimpleFormatter());
        julLogger.addHandler(fileHandler);
    }

    private static double measurePerformance(String loggerName, Runnable logMethod) {
        long startTime = System.nanoTime();
        for (int i = 0; i < LOG_COUNT; i++) {
            logMethod.run();
        }
        long elapsedTime = System.nanoTime() - startTime;
        return elapsedTime / 1e9;
    }
}
