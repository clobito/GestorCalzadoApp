/* Proyecto Software Gestión de Manufactura
Biblioteca de funciones 
Fecha creado: 17/09/2014
Fecha actualizado: 18/09/2014
Cambio realizado: Configuración del componente fecha empleando datepicker como plugin de jquery.
Observaciones: Componente Datepicker en español en http://www.bufa.es/jquery-ui-datepicker-espanol/
*/

$(document).ready(function()
{
	$('#id_Fecha').datepicker({		
		language: 'es',
		closeText: 'Cerrar',
		defaultDate: '+0',
		maxDate: '+8d',
		minDate: '0d',		
		monthNames: ["Enero",
		"Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
		monthNamesShort: ['Ene','Feb','Mar','Abr', 'May','Jun','Jul','Ago','Sep', 'Oct','Nov','Dic'],
		dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
        dayNamesShort: ['Dom','Lun','Mar','Mie','Jue','Vie','Sab'],
		dayNamesMin: ['Do','Lu','Ma','Mi','Ju','Vi','Sa'],
		showWeek: 'True',
		dateFormat: 'yy-mm-dd',
		firstDay: 1,
	});
});
/* Métodos del template base.html 
Fecha actualizado: 18/09/2014
*/

function activar(capa){
	//var u;
	var capa_actual=capa;
	//$("#menu").hide();
	//oculta el menu
	document.getElementById("menu").className="navbar-collapse collapse";//para interfaz movil, retrae menu
	desactivar();
	if(document.getElementById(capa_actual).className=="container hidden"){
		document.getElementById(capa_actual).className="container";
		document.getElementById(capa_actual).disabled=false;
		
		}
		
	else if(document.getElementById(capa_actual).className=="container"){
		document.getElementById(capa_actual).className="container hidden";
		document.getElementById(capa_actual).disabled=true;
		
		}	
		
}

function desactivar(){
	//desactiva las capas visuales del menu principal
		document.getElementById("admin_principal").className="container hidden";
		document.getElementById("admin_principal").disabled=true;
		document.getElementById("gestionInv_principal").className="container hidden";
		document.getElementById("gestionInv_principal").disabled=true;
		document.getElementById("gestionFact_principal").className="container hidden";
		document.getElementById("gestionFact_principal").disabled=true;
		document.getElementById("gestionCostos_principal").className="container hidden";
		document.getElementById("gestionCostos_principal").disabled=true;
		document.getElementById("gestionProdProg_principal").className="container hidden";
		document.getElementById("gestionProdProg_principal").disabled=true;
		document.getElementById("gestionProdFlujos_principal").className="container hidden";
		document.getElementById("gestionProdFlujos_principal").disabled=true;		
	}

function regresa()
{
	/*Fecha creado: 08/09/2014
	Propósito: Regresar al listado después de ingresar detalle de compra.
	FUENTE: https://docs.djangoproject.com/en/dev/topics/http/urls/
	Fecha actualizado: 17/09/2014 
	Cambio realizado: Desactivar metodo, ya que se invoca directamente en el evento.
	Fecha actualizado: 19/09/2014
	Cambio realizado: Se activa método en la vista crear_detalle_compra.html */				
	
	//location.href='{% url "inventario" %}';
	location.href='../../inventario/';
}	
