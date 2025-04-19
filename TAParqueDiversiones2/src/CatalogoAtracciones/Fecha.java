package CatalogoAtracciones;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

public class Fecha {
    private LocalDate fecha;

    public Fecha(String fechaStr) {
        try {
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
            this.fecha = LocalDate.parse(fechaStr, formatter);
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("Formato de fecha inválido. Usa yyyy-MM-dd");
        }
    }

    public LocalDate getFecha() {
        return fecha;
    }

    @Override
    public String toString() {
        return fecha.toString();
    }
}
