package com.example.studentmanagement.service;

import com.example.studentmanagement.entity.Student;
import com.example.studentmanagement.repository.StudentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Collection;
import java.util.List;
import java.util.Optional;

/**
 * Couche de Service contenant la logique métier de l'application.
 * Fait l'intermédiaire entre le contrôleur REST et la couche DAO (StudentRepository).
 */
@Service
public class StudentService {

    @Autowired
    private StudentRepository studentRepository;

    /**
     * Enregistre ou met à jour un étudiant dans la base de données.
     * 
     * @param student l'étudiant à sauvegarder
     * @return l'étudiant sauvegardé avec son identifiant généré
     */
    public Student save(Student student) {
        return studentRepository.save(student);
    }

    /**
     * Supprime un étudiant à partir de son identifiant.
     * 
     * @param id l'identifiant de l'étudiant
     * @return true si l'étudiant a été trouvé et supprimé, false sinon
     */
    public boolean delete(int id) {
        Optional<Student> studentOptional = Optional.ofNullable(studentRepository.findById(id));
        if (studentOptional.isPresent()) {
            studentRepository.delete(studentOptional.get());
            return true;
        } else {
            return false;
        }
    }

    /**
     * Récupère la liste de tous les étudiants.
     * 
     * @return liste des étudiants
     */
    public List<Student> findAll() {
        return studentRepository.findAll();
    }

    /**
     * Compte le nombre total d'étudiants enregistrés.
     * 
     * @return nombre total d'étudiants
     */
    public long countStudents() {
        return studentRepository.count();
    }

    /**
     * Retourne la répartition des étudiants par année de naissance.
     * 
     * @return collection de statistiques [Année, Nombre]
     */
    public Collection<?> findNbrStudentByYear() {
        return studentRepository.findNbrStudentByYear();
    }
}
