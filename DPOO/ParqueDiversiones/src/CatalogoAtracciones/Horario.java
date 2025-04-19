package CatalogoAtracciones;

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

public class Horario {
    private LocalTime hora;

    public Horario(String horaStr) {
        try {
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm");
            this.hora = LocalTime.parse(horaStr, formatter);
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("Formato de hora inválido (HH:mm)");
        }
    }

    public LocalTime getHora() {
        return hora;
    }

    @Override
    public String toString() {
        return hora.toString();
    }
}

