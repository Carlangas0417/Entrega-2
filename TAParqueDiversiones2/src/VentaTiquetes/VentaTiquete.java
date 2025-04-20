package VentaTiquetes;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import GestionEmpleados.Cliente;
import Util.Fecha;

public abstract class VentaTiquete implements Serializable {

    private static final long serialVersionUID = 1L;

    private boolean esEmpleado;
    private List<Tiquete> tiquetesVendidos;

    public VentaTiquete(boolean esEmpleado) {
        this.esEmpleado = esEmpleado;
        this.tiquetesVendidos = new ArrayList<>();
    }

    public boolean isEmpleado() {
        return esEmpleado;
    }

    public void setEsEmpleado(boolean esEmpleado) {
        this.esEmpleado = esEmpleado;
    }

    public List<Tiquete> getTiquetesVendidos() {
        return tiquetesVendidos;
    }

    public void setTiquetesVendidos(List<Tiquete> tiquetesVendidos) {
        this.tiquetesVendidos = tiquetesVendidos;
    }

    public Tiquete venderTiquete(Cliente cliente, String exclusividad, List<TipoTiquete> modalidades) {
        Fecha fechaVenta = new Fecha(1, 1, 2025); 
        Tiquete tiquete = new Tiquete(fechaVenta, exclusividad) {

			private static final long serialVersionUID = 1L;}; 
        for (TipoTiquete tipo : modalidades) {
            tiquete.agregarModalidad(tipo);
        }

        // Asignar al cliente
        // cliente.agregarTiquete(tiquete);??

        tiquetesVendidos.add(tiquete);

        return tiquete;
    }

    public List<Tiquete> obtenerTiquetesCliente(Cliente cliente) {
        return cliente.getTiquetesDisponibles();
    }
}
