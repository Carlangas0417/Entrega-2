package GestionEmpleados;

public class Turno {
	
	private String horaEntrada;
	private String horaSalida;
	
	public Turno(String horaEntrada, String horaSalida) {
		this.horaEntrada = horaEntrada;
		this.horaSalida = horaSalida;
	}
	
	public String getHoraEntrada() {
		return horaEntrada;
	}

	public String getHoraSalida() {
		return horaSalida;
	}
	
	
}
