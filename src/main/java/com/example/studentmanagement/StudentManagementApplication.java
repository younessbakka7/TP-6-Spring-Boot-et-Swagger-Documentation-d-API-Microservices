package com.example.studentmanagement;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Point d'entrée principal de l'application Spring Boot.
 * Active la configuration automatique, le composant scanning et démarre le serveur web embarqué Tomcat.
 */
@SpringBootApplication
public class StudentManagementApplication {

    public static void main(String[] args) {
        SpringApplication.run(StudentManagementApplication.class, args);
    }
}
