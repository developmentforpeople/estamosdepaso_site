frappe.pages['pagina-nueva-sólo-ed'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'nombre',
		single_column: true
	});
}