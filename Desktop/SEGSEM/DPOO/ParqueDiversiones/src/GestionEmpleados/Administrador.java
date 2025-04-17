package GestionEmpleados;

import java.util.List;

import CatalogoAtracciones.Mecanica;
import Exceptions.AsignacionInvalidaException;

public class Administrador extends Empleado {

    public Administrador(String nombre, String id, String password, String login, List<Turno> turnosAsignados) {
        super(nombre, id, password, login, turnosAsignados);
    }

    public void asignarOperador(Operador operador, Mecanica mecanica) throws AsignacionInvalidaException {
        if (mecanica.getNivelRiesgo().equals("ALTO")) {
            if (!operador.isRiesgoAlto()) {
                throw new AsignacionInvalidaException("El operador no está autorizado para atracciones de riesgo alto.\n");
            }
            if (!operador.getAtraccionesEntrenado().contains(mecanica.id)) {
                throw new AsignacionInvalidaException("El operador no está entrenado para esta atracción.\n");
            }
            mecanica.agregarEmpleado(operador);
            System.out.println("Operador asignado con éxito.\n");
        } 
        
        else if (mecanica.getNivelRiesgo().equals("MEDIO")) {
            mecanica.agregarEmpleado(operador);
            System.out.println("Operador asignado con éxito.\n");
        } 
        
        else {
            throw new AsignacionInvalidaException("Nivel de riesgo no reconocido o acceso denegado.\n");
        }
        operador.anadirAtraccionEntrenado(mecanica.id);
    }

    
}
