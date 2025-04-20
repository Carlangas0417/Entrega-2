package Util;

import java.io.Serializable;

public class RangoFechas implements Serializable {

    private static final long serialVersionUID = 1L;

    private Fecha inicio;
    private Fecha fin;

    public RangoFechas(Fecha inicio, Fecha fin) {
        if (inicio == null || fin == null) {
            throw new IllegalArgumentException("Las fechas no pueden ser nulas.");
        }
        if (fin.esAnteriorA(inicio)) {
            throw new IllegalArgumentException("La fecha de fin debe ser igual o posterior a la de inicio.");
        }
        this.inicio = inicio;
        this.fin = fin;
    }

    public Fecha getInicio() {
        return inicio;
    }

    public Fecha getFin() {
        return fin;
    }

    public void setInicio(Fecha inicio) {
        this.inicio = inicio;
    }

    public void setFin(Fecha fin) {
        this.fin = fin;
    }

    public boolean incluye(Fecha f) {
        return !f.esAnteriorA(inicio) && !f.esPosteriorA(fin);
    }
}
