package com.inmemorycache.cachedemo;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/cache")
public class CacheDemo {
    Logger Log = LoggerFactory.getLogger(CacheDemo.class);

    @GetMapping("/test")
    @Cacheable("some-name")
    public String demonstrateCache() throws InterruptedException {
        Log.info("Hey I'm here waiting for the thread sleep");
        Thread.sleep(3000);
        Log.info("It's done");
        return "working";
    }

    @CacheEvict(value = "some-name", allEntries = true)
    @Scheduled(fixedRateString = "20000")
    public void evictCache() {
        // Intentionally blank
        Log.info("emptying cache");
    }

}
