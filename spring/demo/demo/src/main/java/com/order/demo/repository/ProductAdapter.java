package com.order.demo.repository;

import com.order.demo.Product;
import org.springframework.stereotype.Component;

@Component
public class ProductAdapter implements ProductPort {
    protected final MemoryRepository memoryRepository;

    public ProductAdapter(MemoryRepository memoryRepository) {
        this.memoryRepository = memoryRepository;
    }

    @Override
    public void save(Product product) {
        memoryRepository.save(product);
    }
}
