package GestionEmpleados;

public class Turno {
	
	private int horaEntrada;
	private int horaSalida;
	
	public Turno(int horaEntrada, int horaSalida) {
		this.horaEntrada = horaEntrada;
		this.horaSalida = horaSalida;
	}
	
	public int getHoraEntrada() {
		return horaEntrada;
	}

	public int getHoraSalida() {
		return horaSalida;
	}
	
	
}
