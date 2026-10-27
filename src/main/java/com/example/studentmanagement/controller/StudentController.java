package com.example.studentmanagement.controller;

import com.example.studentmanagement.entity.Student;
import com.example.studentmanagement.service.StudentService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Collection;
import java.util.List;

/**
 * Contrôleur REST exposant les endpoints de l'API de gestion des étudiants.
 * Documenté avec Swagger / OpenAPI (springdoc-openapi).
 */
@RestController
@RequestMapping("students")
@Tag(name = "Student Controller", description = "Gestion complète des étudiants et des statistiques associées")
public class StudentController {

    @Autowired
    private StudentService studentService;

    /**
     * Enregistre un nouvel étudiant ou met à jour un étudiant existant.
     * 
     * @param student les informations de l'étudiant
     * @return l'étudiant créé avec le statut HTTP 201 Created
     */
    @Operation(summary = "Enregistrer un étudiant", description = "Permet de créer un nouvel étudiant ou de modifier un étudiant existant")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "201", description = "Étudiant ajouté avec succès"),
            @ApiResponse(responseCode = "400", description = "Données d'étudiant invalides")
    })
    @PostMapping("/save")
    public ResponseEntity<Student> save(
            @Parameter(description = "Objet JSON contenant les informations de l'étudiant", required = true)
            @RequestBody Student student) {
        Student savedStudent = studentService.save(student);
        return new ResponseEntity<>(savedStudent, HttpStatus.CREATED);
    }

    /**
     * Supprime un étudiant à partir de son identifiant.
     * 
     * @param id l'identifiant de l'étudiant à supprimer
     * @return 204 No Content si supprimé, 404 Not Found si inexistant
     */
    @Operation(summary = "Supprimer un étudiant", description = "Supprime définitivement un étudiant selon son identifiant unique")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "204", description = "Étudiant supprimé avec succès"),
            @ApiResponse(responseCode = "404", description = "Étudiant non trouvé")
    })
    @DeleteMapping("/delete/{id}")
    public ResponseEntity<Void> delete(
            @Parameter(description = "Identifiant de l'étudiant à supprimer", required = true, example = "1")
            @PathVariable("id") int id) {
        boolean deleted = studentService.delete(id);
        if (deleted) {
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    /**
     * Récupère la liste complète de tous les étudiants.
     * 
     * @return liste des étudiants avec le statut HTTP 200 OK
     */
    @Operation(summary = "Récupérer tous les étudiants", description = "Renvoie la liste exhaustive de tous les étudiants enregistrés")
    @ApiResponse(responseCode = "200", description = "Liste complète des étudiants renvoyée")
    @GetMapping("/all")
    public ResponseEntity<List<Student>> findAll() {
        List<Student> students = studentService.findAll();
        return new ResponseEntity<>(students, HttpStatus.OK);
    }

    /**
     * Retourne le nombre total d'étudiants enregistrés dans l'application.
     * 
     * @return total des étudiants avec le statut HTTP 200 OK
     */
    @Operation(summary = "Compter les étudiants", description = "Retourne le nombre total d'étudiants enregistrés dans la base de données")
    @ApiResponse(responseCode = "200", description = "Nombre total d'étudiants renvoyé")
    @GetMapping("/count")
    public ResponseEntity<Long> countStudent() {
        long count = studentService.countStudents();
        return new ResponseEntity<>(count, HttpStatus.OK);
    }

    /**
     * Retourne les statistiques du nombre d'étudiants regroupés par année de naissance.
     * 
     * @return collection d'éléments [Année, Nombre] avec le statut HTTP 200 OK
     */
    @Operation(summary = "Statistiques des étudiants par année", description = "Agrège et compte le nombre d'étudiants nés pour chaque année")
    @ApiResponse(responseCode = "200", description = "Répartition des étudiants par année de naissance")
    @GetMapping("/byYear")
    public ResponseEntity<Collection<?>> findByYear() {
        Collection<?> studentsByYear = studentService.findNbrStudentByYear();
        return new ResponseEntity<>(studentsByYear, HttpStatus.OK);
    }
}
