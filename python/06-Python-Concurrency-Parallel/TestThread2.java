package com.darrenchan.thread;

public class TestThread {
public static void main(String[] args) {
for (int i = 0; i < 3; i++) {
new Thread(new Runnable() {

            @Override
            public void run() {
                while (true) {

                }
            }
        }).start();
    }
    while(true){

    }
}
}