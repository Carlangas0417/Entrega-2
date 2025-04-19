package CatalogoAtracciones;

import java.util.List;

public class Espectaculo {
    public List<Horario> horarios;
    public List<Fecha> fechas;
    public boolean disponibilidad;

    public Espectaculo(List<Horario> horarios, List<Fecha> fechas, boolean disponibilidad) {
        this.horarios = horarios;
        this.fechas = fechas;
        this.disponibilidad = disponibilidad;
    }
    
    public void mostrarEspectaculo() {
        System.out.println("Detalles del Espectáculo:");
        
        if (fechas != null && !fechas.isEmpty()) {
            System.out.println("Fechas disponibles:");
            for (Fecha fecha : fechas) {
                System.out.println("- " + fecha.toString());
            }
        } else {
            System.out.println("No hay fechas disponibles.");
        }

        if (horarios != null && !horarios.isEmpty()) {
            System.out.println("Horarios disponibles:");
            for (Horario horario : horarios) {
                System.out.println("- " + horario.toString());
            }
        } else {
            System.out.println("No hay horarios disponibles.");
        }

        System.out.println("Disponibilidad actual: " + (disponibilidad ? "Sí" : "No"));
    }

}
