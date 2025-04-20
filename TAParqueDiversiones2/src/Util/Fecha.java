package Util;

import java.io.Serializable;
import java.util.Objects;

public class Fecha implements Serializable {

    private static final long serialVersionUID = 1L;

    private int dia;
    private int mes;
    private int anio;

    public Fecha(int dia, int mes, int anio) {
        if (!esFechaValida(dia, mes, anio)) {
            throw new IllegalArgumentException("Fecha inválida.");
        }
        this.dia = dia;
        this.mes = mes;
        this.anio = anio;
    }

    public int getDia() {
        return dia;
    }

    public int getMes() {
        return mes;
    }

    public int getAnio() {
        return anio;
    }

    public boolean esAnteriorA(Fecha otra) {
        if (this.anio < otra.anio) return true;
        if (this.anio == otra.anio && this.mes < otra.mes) return true;
        if (this.anio == otra.anio && this.mes == otra.mes && this.dia < otra.dia) return true;
        return false;
    }

    public boolean esPosteriorA(Fecha otra) {
        if (this.anio > otra.anio) return true;
        if (this.anio == otra.anio && this.mes > otra.mes) return true;
        if (this.anio == otra.anio && this.mes == otra.mes && this.dia > otra.dia) return true;
        return false;
    }

    public boolean esIgualA(Fecha otra) {
        return this.dia == otra.dia && this.mes == otra.mes && this.anio == otra.anio;
    }

    private boolean esFechaValida(int d, int m, int a) {
        if (m < 1 || m > 12 || d < 1) return false;
        int[] diasPorMes = { 31, (esBisiesto(a) ? 29 : 28), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        return d <= diasPorMes[m - 1];
    }

    private boolean esBisiesto(int anio) {
        return (anio % 4 == 0 && anio % 100 != 0) || (anio % 400 == 0);
    }

    @Override
    public String toString() {
        return String.format("%02d/%02d/%04d", dia, mes, anio);
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Fecha)) return false;
        Fecha otra = (Fecha) obj;
        return this.dia == otra.dia && this.mes == otra.mes && this.anio == otra.anio;
    }

    @Override
    public int hashCode() {
        return Objects.hash(dia, mes, anio);
    }
}
