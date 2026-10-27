package com.example.studentmanagement;

import com.example.studentmanagement.controller.StudentController;
import com.example.studentmanagement.entity.Student;
import com.example.studentmanagement.service.StudentService;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import java.util.Arrays;
import java.util.Collection;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;

/**
 * Tests unitaires automatisés pour StudentController avec JUnit 5 et Mockito.
 * Valide le comportement du contrôleur REST de manière isolée sans base de données réelle (Étape 8).
 */
@SpringBootTest
class StudentControllerTest {

    @Mock
    private StudentService studentService;

    @InjectMocks
    private StudentController studentController;

    @Test
    @DisplayName("Test 1: Enregistrement d'un étudiant (201 Created)")
    void testSaveStudent() {
        Student student = new Student();
        student.setId(1);
        student.setNom("Mido");

        when(studentService.save(any(Student.class))).thenReturn(student);

        ResponseEntity<Student> response = studentController.save(student);

        assertEquals(HttpStatus.CREATED, response.getStatusCode());
        assertNotNull(response.getBody());
        assertEquals("Mido", response.getBody().getNom());
    }

    @Test
    @DisplayName("Test 2: Suppression d'un étudiant existant (204 No Content)")
    void testDeleteStudent() {
        when(studentService.delete(1)).thenReturn(true);

        ResponseEntity<Void> response = studentController.delete(1);

        assertEquals(HttpStatus.NO_CONTENT, response.getStatusCode());
    }

    @Test
    @DisplayName("Test 3: Suppression d'un étudiant inexistant (404 Not Found)")
    void testDeleteStudentNotFound() {
        when(studentService.delete(999)).thenReturn(false);

        ResponseEntity<Void> response = studentController.delete(999);

        assertEquals(HttpStatus.NOT_FOUND, response.getStatusCode());
    }

    @Test
    @DisplayName("Test 4: Récupération de tous les étudiants (200 OK)")
    void testFindAllStudents() {
        Student student1 = new Student();
        Student student2 = new Student();
        when(studentService.findAll()).thenReturn(Arrays.asList(student1, student2));

        ResponseEntity<List<Student>> response = studentController.findAll();

        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertNotNull(response.getBody());
        assertEquals(2, response.getBody().size());
    }

    @Test
    @DisplayName("Test 5: Comptage total des étudiants (200 OK)")
    void testCountStudents() {
        when(studentService.countStudents()).thenReturn(10L);

        ResponseEntity<Long> response = studentController.countStudent();

        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertEquals(10L, response.getBody());
    }

    @Test
    @DisplayName("Test 6: Statistiques des étudiants par année (200 OK)")
    void testFindByYear() {
        when(studentService.findNbrStudentByYear()).thenReturn(Arrays.asList());

        ResponseEntity<Collection<?>> response = studentController.findByYear();

        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertNotNull(response.getBody());
        assertEquals(0, response.getBody().size());
    }
}
