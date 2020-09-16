function dragElement(elmnt) {
  var pos1 = 0,
      pos2 = 0,
      pos3 = 0,
      pos4 = 0; // console.log(elmnt)

  if (elmnt) {
    /* if present, the header is where you move the DIV from:*/
    elmnt.onmousedown = dragMouseDown;
  } else {
    /* otherwise, move the DIV from anywhere inside the DIV:*/
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault(); // get the mouse cursor position at startup:

    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement; // call a function whenever the cursor moves:

    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault(); // calculate the new cursor position:

    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY; // set the element's new position:

    elmnt.style.top = elmnt.offsetTop - pos2 + "px";
    elmnt.style.left = elmnt.offsetLeft - pos1 + "px";
  }

  function closeDragElement() {
    /* stop moving when mouse button is released:*/
    document.onmouseup = null;
    document.onmousemove = null;
  }
}

$(document).ready(function () {
  $('.window').each(function (idx, el) {
    dragElement(el);
    $('.app-icon').unbind('click tap touch').on('click tap touch', function (el) {
      el.preventDefault();
      console.log('click');

      if ($(this).hasClass('selected')) {
        $(this).removeClass('selected');
      } else {
        $('.app-icon').removeClass('selected');
        $(this).addClass('selected');
      } // if( 'info' === $(this).data('app')){
      //   alert('message?: DOMString')
      // }

    });
    $('.app-icon').unbind('dblclick doubletap').on('dblclick doubletap', function (el) {
      el.preventDefault(); // $(this).toggleClass('selected')
      // if( 'info' === $(this).data('app')){
      //   alert($(this).data('app'))
      // }

      $('.window[data-app=' + $(this).data('app') + ']').show();
    });
  });
  $('.window.message .close').unbind('click tap touch').on('click tap touch', function () {
    $(this).parent().parent().hide();
  });
});