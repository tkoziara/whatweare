/* Based on
 * https://github.com/evaldsurtans/maintainscroll.jquery.js
 */

function getPageName() {
	var path = window.location.pathname;
	var page = path.split("/").pop();
	var page_name = page.split(".")[0];
	return page_name;
}

document.addEventListener('DOMContentLoaded', function() {
	var cookie = getPageName() + '_scrollY';

	window.addEventListener('pagehide', function(e) {
		setCookie(cookie,window.scrollY,365);
	});

	var scrollY = getCookie(cookie);

	if(scrollY != "")
	{
		window.scrollTo(0, scrollY);
	}
});