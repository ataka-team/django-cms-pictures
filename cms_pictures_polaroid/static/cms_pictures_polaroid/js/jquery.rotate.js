/*!
 * jQuery rotate - v0.1 - 30/03/2011
 * http://www.etnassoft.com
 *
 * Copyright (c) 2011 Carlos Benitez | EtnasSoft
 * Dual licensed under the MIT and GPL licenses.
 * http://www.etnassoft.com/licencias/
 */

 (function($) {

 $.fn.rotate = function( options ) {

  // Default options
  var defaults = {
    angle: 0,
    center: true
  };

  // Extend our default options with those provided.
  var opts = $.extend(defaults, options);

  // Precaching the user browser
  var isIE = ( navigator.userAgent.match( /MSIE/i ) ) ? true : false;

  // Return
  return this.each(function() {
    $this = $(this);

    // Continue as browser
    ( isIE ) ? IE( $this ) : nonIE( $this );
  });

  // Non IE Browser
  function nonIE( $this ){
    $this.css('transform', 'rotate(' + opts.angle + 'deg)');
    $this.css('-moz-transform', 'rotate(' + opts.angle + 'deg)');
    $this.css('-o-transform', 'rotate(' + opts.angle + 'deg)');
    $this.css('-webkit-transform', 'rotate(' + opts.angle + 'deg)');
  }

  // IE Browser
  function IE( $this ){
    var angle = opts.angle,
        rad = angle * Math.PI * 2 / 360,
        cos = Math.cos(rad),
        sin = Math.sin(rad);

    var obj = $this[0],
        objPos = $this.css('position'),
        objHeight = obj.clientHeight,
        objWidth = obj.clientWidth,
        objTop = parseInt( $this.css('top'), 10 ) || 1,
        objLeft = parseInt( $this.css('left'), 10 ) || 1;

    if( !$this.data('origTop') ) $this.data( 'origTop', objTop );
    if( !$this.data('origLeft') ) $this.data( 'origLeft', objLeft );

    obj.style.filter = "progid:DXImageTransform.Microsoft.Matrix();";
    obj.filters.item("DXImageTransform.Microsoft.Matrix").SizingMethod = "auto expand";
    obj.filters.item("DXImageTransform.Microsoft.Matrix").FilterType = "bilinear";
    obj.filters.item("DXImageTransform.Microsoft.Matrix").M11 = cos;
    obj.filters.item("DXImageTransform.Microsoft.Matrix").M12 = (-sin);
    obj.filters.item("DXImageTransform.Microsoft.Matrix").M21 = sin;
    obj.filters.item("DXImageTransform.Microsoft.Matrix").M22 = cos;

    // Center axis
    if(opts.center){
      if (objPos != 'absolute' && objPos != 'fixed') $this.css('position', 'relative');
      obj.style.top = $this.data('origTop') + ( ( objHeight - obj.offsetHeight ) / 2 ) + 'px';
      obj.style.left = $this.data('origLeft') + ( ( objWidth - obj.offsetWidth ) / 2 ) + 'px';
    }

  }

 };

 })(jQuery);