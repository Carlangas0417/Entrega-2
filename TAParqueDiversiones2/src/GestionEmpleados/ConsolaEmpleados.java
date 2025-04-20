package GestionEmpleados;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import ConsolaGeneral.CGeneral;
import Tiquetes.Tiquete;

public  class ConsolaEmpleados extends CGeneral {
	
    	Administrador elAdmin = new Administrador("elAdmin", "eladmin", "el.admin", null);

	    public void iniciarConsola() throws IOException {
	    	
	    	BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	        boolean terminado = false;

	        while (!terminado) {
		        System.out.println("Seleccione el tipo de usuario:");
		        System.out.println("1. Cliente");
		        System.out.println("2. Empleado");
		        System.out.println("3. Administrador");
		       
		        
		        String anteopcion = reader.readLine();
		        
		        if (anteopcion.equals("1")) { //cliente
		        	anteConsolaClientes();
	            } 
		        else if (anteopcion.equals("2")) { //empleado
		        	
	            } 
		        else if (anteopcion.equals("3")) { //administrador
		        	anteConsolaAdministrador();
	            } 
	            else {
	                System.out.println("La opción digitada no es válida.");
	            }

	        }
	        
	        
	    }
	    
	    public void anteConsolaClientes() throws IOException {
	    	BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	        boolean terminado = false;
	    	
	    	while (!terminado) {
	    		String Popcion = reader.readLine();
				System.out.println("1. Crear cliente");
				System.out.println("2. Ingresar con credenciales");
				if (Popcion.equals("1")) { //Creacion del cliente
				  	consolaCreacionCliente();
				} 
				else if (Popcion.equals("2")) { //Ingreso con credenciales
					consolaVerClienteExistente();
				} 
				else {
					System.out.println("La opción ingresada no es válida. Inténtelo de nuevo.");
				}
	    	}
	    }
	    
	    public void consolaCreacionCliente() throws IOException {
	    	String nombre = cadena("Ingrese su nombre completo");
	        String login = cadena("Cree un nombre de usuario (login)");
	        String password = cadena("Cree una contraseña");

	        try {
	            Usuario cliente = new Cliente(nombre, password, login);
	            System.out.println("¡Cliente creado con éxito!");
	            System.out.println("Nombre: " + cliente.getNombre());
	            System.out.println("ID: " + cliente.getId());
	            System.out.println("Login: " + cliente.getLogin());
	        } catch (IllegalArgumentException e) {
	            System.out.println(e.getMessage());
	            System.out.println("Intente de nuevo con un login diferente. El seleccionado ya existe");
	        }
	    }
	    
	    public void consolaVerClienteExistente() throws IOException {
	    	System.out.println("Usuarios de los clientes registrados: \n");
	    	if (Cliente.usuariosClientes != null) {
	    	    for (String clave : Cliente.usuariosClientes.keySet()) {
	    	        if (clave != null) {
	    	            System.out.println("-" + clave);
	    	        }
	    	    }
	    	} else {
	    	    System.out.println("Aún no hay clientes registrados.");
	    	}
	    	System.out.println("\n");
	    	String usuario = cadena("Ingrese su usuario");
	    	
	    	boolean terminado = false; 
	    	while (!terminado) {
		    	if (Cliente.usuariosClientes.containsKey(usuario)) {
		    		System.out.println("Bienvenid@ " + Cliente.usuariosClientes.get(usuario));
		    		String contrasena = cadena("Ingrese la contraseña");
		    		if (Cliente.contrasenasClientes.get(usuario).equals(contrasena)) {
		    			System.out.println("La contraseña es correcta.\n");
		    			Cliente cliente = Cliente.clientesInfoCompletitud.get(usuario);
		    			System.out.println("Nombre: " + cliente.getNombre());
			            System.out.println("ID: " + cliente.getId());
			            System.out.println("Login: " + cliente.getLogin());
			            List<Tiquete> tiquetesD = cliente.getTiquetesDisponibles();
			            if (tiquetesD != null && tiquetesD.size() > 0) {
			            	for (int i = 0; i < tiquetesD.size(); i++) {
			            		//PRINTEO DE LOS TIQUETES AAAA.
			            		terminado = true;
							}
			            }
			            else {
			            	System.out.println("Aún no hay tiquetes asociados.");
			            }
		    		}
		    		else {
		    			System.out.println("La contraseña no coincide. ");			
		    			String opcion = cadena("Si desea regresar al menú principal, ingrese 1. De lo contrario oprima cualquier otra tecla");
		    			if (opcion.equals("1")) {
		    				terminado = true; 
		    			}
		    		}
		    	}
		    	else {
		    		System.out.println("El usuario ingresado no está registrado.");
		    		String opcion = cadena("Si desea regresar al menú principal, ingrese 1. De lo contrario oprima cualquier otra tecla");
	    			if (opcion.equals("1")) {
	    				terminado = true; 
	    			}
		    	}
	    	}	    	
	    }
	    
	    public void anteConsolaAdministrador() throws IOException {
	    	boolean terminado = false; 
	    	while (!terminado) {
		    	String usuario = cadena("Ingrese el usuario del administrador");
		    	if (Administrador.usuariosAdmins.containsKey(usuario)) {
		    		System.out.println("Bienvenid@ " + Administrador.usuariosAdmins.get(usuario));
		    		String contrasena = cadena("Ingrese la contraseña");
		    		if (Cliente.contrasenasClientes.get(usuario).equals(contrasena)) {
		    			System.out.println("La contraseña es correcta.\n");
		    			menuAdministrador();
		    		}
		    		else {
		    			System.out.println("La contraseña ingresada no es correcta.");
		    			String opcion = cadena("Si desea regresar al menú principal, ingrese 1. De lo contrario oprima cualquier otra tecla");
		    			if (opcion.equals("1")) {
		    				terminado = true; 
		    			}
		    		}
		    	}
		    	else {
		    		System.out.println("El usuario ingresado no es de un administrador.");
		    		String opcion = cadena("Si desea regresar al menú principal, ingrese 1. De lo contrario oprima cualquier otra tecla");
	    			if (opcion.equals("1")) {
	    				terminado = true; 
	    			}
		    	}
	    	}
	    }
	    
	    

	    public void menuAdministrador() throws IOException {
	        System.out.println("Menú de administrador: \n");
	        System.out.println("1. Crear sitios de trabajo");
	        System.out.println("2. Crear empleado");
	        System.out.println("0. Salir");
	        
	        String opcion = cadena("Seleccione una opción");
	        if (opcion.equals("1")) {
	        	consolaCrearEmpleado();
	        }
	        else if (opcion.equals("2")) {
	        	consolaCrearSitiosTrabajo();
	        }
	    }
	    
	    
	    public void consolaCrearEmpleado() throws IOException {
	    	boolean salir = false;
    	    while (!salir) {
    	        System.out.println("\nSeleccione el tipo de empleado a crear:");
    	        System.out.println("1. Operador");
    	        System.out.println("2. Cajero");
    	        System.out.println("3. Cocinero");
    	        System.out.println("4. Volver al menú principal");
    	        //poner condicionales antes de crear pues no se pueden asignar a lugares de trabajo nulos

    	        String opcion = cadena("Ingrese opción:");

    	        if (opcion.equals("1")) {
    	            crearOperador();
    	        } else if (opcion.equals("2")) {
    	            crearCajero();
    	        } else if (opcion.equals("3")) {
    	            crearCocinero();
    	        } else if (opcion.equals("4")) {
    	            salir = true;
    	            System.out.println("Volviendo al menú principal...");
    	        } else {
    	            System.out.println("Opción no válida. Intente de nuevo.");
    	        }
    	    }
    	}
	    
	    private void crearOperador() throws IOException {
	        String nombre = cadena("Nombre:");
	        String login = cadena("Login:");
	        String password = cadena("Contraseña:");
	        List<Turno> turnos = new ArrayList<>(); 
	        String respuestaRiesgo = cadena("¿Es de riesgo alto? (si/no):");
	        boolean riesgoAlto = respuestaRiesgo.equalsIgnoreCase("si");
	        List<Integer> atraccionesEntrenado = new ArrayList<>();
	        System.out.println("Ingrese los ID de las atracciones en las que está entrenado (escriba 'fin' para terminar):");
	        boolean terminado = false;
	        while (!terminado) {
	            String entrada = cadena("ID:");
	            if (entrada.equalsIgnoreCase("fin")) {
	                terminado = true;
	            } else {
	                try {
	                    int id = Integer.parseInt(entrada);
	                    atraccionesEntrenado.add(id);
	                } catch (NumberFormatException e) {
	                    System.out.println("ID inválido. Intente nuevamente.");
	                }
	            }
	        }
	        int atraccionAsignada = -1;
	        boolean idValido = false;
	        while (!idValido) {
	            atraccionAsignada = natural("Ingrese el ID de la atracción asignada:");
	            if (atraccionesEntrenado.contains(atraccionAsignada)) {
	                idValido = true;
	            } else {
	                System.out.println("El ID ingresado no está en la lista de atracciones entrenadas. Intente nuevamente.");
	            }
	        }
	        Operador operador = new Operador(nombre, password, login, turnos, riesgoAlto, atraccionesEntrenado, atraccionAsignada);
	        System.out.println("¡Operador creado con éxito! \n");
	    }
	    
	    private Cajero crearCajero() throws IOException {
	        String nombre = cadena("Nombre:");
	        String login = cadena("Login:");
	        String password = cadena("Contraseña:");

	        List<Turno> turnos = new ArrayList<>();
	        Cajero cajero = new Cajero(nombre, password, login, turnos, null);
	        System.out.println("Cajero creado exitosamente.");
	        
	        return cajero;
	        //QUIERE ASIGNARLO A UN SITIO DE TRABAJO?
	    }
	    
	    private void crearCocinero() throws IOException {
	        String nombre = cadena("Nombre:");
	        String login = cadena("Login:");
	        String password = cadena("Contraseña:");

	        List<Turno> turnos = new ArrayList<>();
	        Cocinero cocinero = new Cocinero(nombre, password, login, turnos, null);
	        System.out.println("Cocinero creado exitosamente.");
	        //QUIERE ASIGNARLO A UN SITIO DE TRABAJO?
	    }
	    
	    public void consolaCrearSitiosTrabajo() throws IOException {
	        boolean salir = false;

	        while (!salir) {
	            System.out.println("\nSeleccione el tipo de lugar de servicio:");
	            System.out.println("1. Taquilla");
	            System.out.println("2. Tienda");
	            System.out.println("3. Cafetería");
	            System.out.println("4. Volver al menú principal");

	            String opcion = cadena("Ingrese opción:");

	            if (opcion.equals("1")) {
	                crearTaquilla();
	            } else if (opcion.equals("2")) {
	                crearTienda();
	            } else if (opcion.equals("3")) {
	                crearCafeteria();
	            } else if (opcion.equals("4")) {
	                salir = true;
	                System.out.println("Volviendo al menú principal...");
	            } else {
	                System.out.println("Opción inválida. Intente nuevamente.");
	            }
	        }
	    }
	    
	    private void crearTaquilla() throws IOException {
	        String nombre = cadena("Nombre de la taquilla:");
	        String ubicacion = cadena("Ubicación de la taquilla:");
	        Taquilla taquilla = new Taquilla(null, ubicacion, nombre);
	        System.out.println("Taquilla creada exitosamente.");
	    }
	    
	    private void crearTienda() throws IOException {
	        String nombre = cadena("Nombre de la tienda:");
	        String ubicacion = cadena("Ubicación de la tienda:");
	        Tienda tienda = new Tienda(null, ubicacion, nombre);
	        System.out.println("Tienda creada exitosamente.");
	    }
	    
	    private void crearCafeteria() throws IOException {
	        String nombre = cadena("Nombre de la cafetería:");
	        String ubicacion = cadena("Ubicación de la cafetería:");
	        Cafeteria cafeteria = new Cafeteria(null, ubicacion, null, nombre);
	        System.out.println("Cafetería creada exitosamente");
	    }







	    

}

	
	

