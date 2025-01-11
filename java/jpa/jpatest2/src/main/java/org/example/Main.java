package org.example;

import jakarta.persistence.*;
import org.example.domain.Course;
import org.example.domain.Student;
import org.hibernate.Hibernate;
import org.hibernate.Session;
import org.hibernate.stat.Statistics;

import java.util.List;

public class Main {
    public static void main(String[] args) {

        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();

        EntityTransaction tx = em.getTransaction();


        try {
            tx.begin();

            Course course  = em.createQuery("Select c from Course c where c.courseId = :id", Course.class)
                    .setParameter("id", 1L)
                    .getSingleResult();

            System.out.println(course.getProfessor().getClass());

            tx.commit();
        } catch (Exception e) {
            tx.rollback();
            e.printStackTrace();
        } finally {
            em.close();
        }

        emf.close();

    }
}