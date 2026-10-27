package com.example.studentmanagement.repository;

import com.example.studentmanagement.entity.Student;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.Collection;

/**
 * Interface Repository assurant la persistance des données pour l'entité Student.
 * Étend JpaRepository pour bénéficier des méthodes standards CRUD et de pagination.
 */
@Repository
public interface StudentRepository extends JpaRepository<Student, Integer> {

    /**
     * Recherche d'un étudiant par son identifiant unique.
     * 
     * @param id identifiant de l'étudiant
     * @return l'étudiant trouvé ou null
     */
    Student findById(int id);

    /**
     * Requête JPQL personnalisée regroupant et comptant les étudiants par année de naissance.
     * 
     * @return Collection de tableaux d'objets [Année, Nombre d'étudiants]
     */
    @Query("SELECT YEAR(s.dateNaissance), COUNT(s) FROM Student s GROUP BY YEAR(s.dateNaissance)")
    Collection<Object[]> findNbrStudentByYear();
}
