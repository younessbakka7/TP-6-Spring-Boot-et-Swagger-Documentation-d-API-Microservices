package com.example.studentmanagement.entity;

import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.persistence.*;
import java.util.Date;

/**
 * Entité JPA représentant un étudiant dans l'application.
 * Mappée à la table 'student' dans la base de données relationnelle.
 */
@Entity
@Table(name = "student")
@Schema(description = "Entité représentant un étudiant avec ses informations personnelles")
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Schema(description = "Identifiant unique de l'étudiant auto-incrémenté", example = "1")
    private int id;

    @Schema(description = "Nom de famille de l'étudiant", example = "LACHGAR")
    private String nom;

    @Schema(description = "Prénom de l'étudiant", example = "Mohamed")
    private String prenom;

    @Temporal(TemporalType.DATE)
    @Schema(description = "Date de naissance de l'étudiant au format YYYY-MM-DD", example = "1985-09-01")
    private Date dateNaissance;

    // Constructeur sans argument obligatoire pour JPA
    public Student() {
    }

    // Constructeur avec nom, prénom et date de naissance
    public Student(String nom, String prenom, Date dateNaissance) {
        this.nom = nom;
        this.prenom = prenom;
        this.dateNaissance = dateNaissance;
    }

    // Constructeur complet avec identifiant
    public Student(int id, String nom, String prenom, Date dateNaissance) {
        this.id = id;
        this.nom = nom;
        this.prenom = prenom;
        this.dateNaissance = dateNaissance;
    }

    // Getters et Setters
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }

    public Date getDateNaissance() {
        return dateNaissance;
    }

    public void setDateNaissance(Date dateNaissance) {
        this.dateNaissance = dateNaissance;
    }

    @Override
    public String toString() {
        return "Student{" +
                "id=" + id +
                ", nom='" + nom + '\'' +
                ", prenom='" + prenom + '\'' +
                ", dateNaissance=" + dateNaissance +
                '}';
    }
}
