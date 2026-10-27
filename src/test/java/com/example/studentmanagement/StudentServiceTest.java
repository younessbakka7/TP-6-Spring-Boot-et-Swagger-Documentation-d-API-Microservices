package com.example.studentmanagement;

import com.example.studentmanagement.entity.Student;
import com.example.studentmanagement.repository.StudentRepository;
import com.example.studentmanagement.service.StudentService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.*;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

/**
 * Tests unitaires pour la couche StudentService.
 */
@ExtendWith(MockitoExtension.class)
class StudentServiceTest {

    @Mock
    private StudentRepository studentRepository;

    @InjectMocks
    private StudentService studentService;

    private Student student;

    @BeforeEach
    void setUp() {
        student = new Student(1, "LACHGAR", "Mohamed", new Date());
    }

    @Test
    @DisplayName("Service: Sauvegarder un étudiant")
    void testSave() {
        when(studentRepository.save(any(Student.class))).thenReturn(student);

        Student saved = studentService.save(student);

        assertNotNull(saved);
        assertEquals("LACHGAR", saved.getNom());
        assertEquals("Mohamed", saved.getPrenom());
        verify(studentRepository, times(1)).save(student);
    }

    @Test
    @DisplayName("Service: Supprimer avec succès")
    void testDeleteSuccess() {
        when(studentRepository.findById(1)).thenReturn(student);
        doNothing().when(studentRepository).delete(student);

        boolean result = studentService.delete(1);

        assertTrue(result);
        verify(studentRepository, times(1)).delete(student);
    }

    @Test
    @DisplayName("Service: Supprimer un étudiant inexistant")
    void testDeleteNotFound() {
        when(studentRepository.findById(99)).thenReturn(null);

        boolean result = studentService.delete(99);

        assertFalse(result);
        verify(studentRepository, never()).delete(any());
    }

    @Test
    @DisplayName("Service: Récupérer tous les étudiants")
    void testFindAll() {
        List<Student> list = List.of(student, new Student(2, "BENANI", "Ali", new Date()));
        when(studentRepository.findAll()).thenReturn(list);

        List<Student> result = studentService.findAll();

        assertEquals(2, result.size());
        verify(studentRepository, times(1)).findAll();
    }

    @Test
    @DisplayName("Service: Compter les étudiants")
    void testCount() {
        when(studentRepository.count()).thenReturn(5L);

        long count = studentService.countStudents();

        assertEquals(5L, count);
        verify(studentRepository, times(1)).count();
    }

    @Test
    @DisplayName("Service: Statistiques par année")
    void testFindNbrStudentByYear() {
        List<Object[]> stats = new ArrayList<>();
        stats.add(new Object[]{1985, 2L});
        stats.add(new Object[]{1990, 1L});
        when(studentRepository.findNbrStudentByYear()).thenReturn(stats);

        Collection<?> result = studentService.findNbrStudentByYear();

        assertEquals(2, result.size());
        verify(studentRepository, times(1)).findNbrStudentByYear();
    }
}
