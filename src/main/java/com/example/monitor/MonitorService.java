package com.example.monitor;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class MonitorService {
    public static void main(String[] args) {
        try {
            Process process = new ProcessBuilder("python3", "src/main/python/monitor.py")
                .redirectErrorStream(true)
                .start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            process.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
