package org.example;

import jakarta.persistence.*;
import org.example.domain.Course;
import org.example.domain.Student;
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
//
//            Course course = em.find(Course.class, 1L);
//            System.out.println(course.getTitle());


            Query query = em.createQuery("select c from Course c join fetch c.professor");
            List<Course> courses = query.getResultList();

            for (Course course: courses) {
                course.getProfessor().getName();
            }
//



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