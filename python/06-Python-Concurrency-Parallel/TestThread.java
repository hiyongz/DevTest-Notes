package com.darrenchan.thread;

public class TestThread {
    public static void main(String[] args) {
        for (int i = 0; i < 2; i++) {
            new Thread(new Runnable() {
                        int n = 100000000;
                        @Override
                        public void run() {
                            while (n>0) {
                                n -= 1;
                            }
                        }
            }).start();
        }

    }
}