// Free to use & distribute under the MIT license
// Wes Johnson (@SterlingWes)
//
// inspired by http://martin.ankerl.com/2009/12/09/how-to-create-random-colors-programmatically/
//and
//https://github.com/sterlingwes/RandomColor/blob/master/rcolor.js


// Random Color:
(function (root, factory) {
    if (typeof exports === 'object') {
        module.exports = factory;
    } else if (typeof define === 'function' && define.amd) {
        define(factory);
    } else {
        root.RColor = factory();
    }
}(this, function () {

        var RColor = function() {
                this.hue                        = Math.random(),
                this.goldenRatio         = 0.618033988749895;
                this.hexwidth                = 2;
        };

        RColor.prototype.hsvToRgb = function (h,s,v) {
                var        h_i        = Math.floor(h*6),
                        f         = h*6 - h_i,
                        p        = v * (1-s),
                        q        = v * (1-f*s),
                        t        = v * (1-(1-f)*s),
                        r        = 255,
                        g        = 255,
                        b        = 255;
                switch(h_i) {
                        case 0:        r = v, g = t, b = p;        break;
                        case 1:        r = q, g = v, b = p;        break;
                        case 2:        r = p, g = v, b = t;        break;
                        case 3:        r = p, g = q, b = v;        break;
                        case 4: r = t, g = p, b = v;        break;
                        case 5: r = v, g = p, b = q;        break;
                }
                return [Math.floor(r*256),Math.floor(g*256),Math.floor(b*256)];
        };
        
        RColor.prototype.padHex = function(str) {
                if(str.length > this.hexwidth) return str;
                return new Array(this.hexwidth - str.length + 1).join('0') + str;
        };
        
        RColor.prototype.get = function(hex,saturation,value) {
                this.hue += this.goldenRatio;
                this.hue %= 1;
                if(typeof saturation !== "number")        saturation = 0.5;
                if(typeof value !== "number")                value = 0.95;
                var rgb = this.hsvToRgb(this.hue,saturation,value);
                if(hex)
                        return "#" +  this.padHex(rgb[0].toString(16))
                                                + this.padHex(rgb[1].toString(16))
                                                + this.padHex(rgb[2].toString(16));
                else 
                        return rgb;
        };

        return RColor;

}));

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
//Create Random Color:
//var randomColor = new RColor;
//var hex = randomColor.get(true);
$(document).ready(function() {

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
//Count Boxes:
var list_items = []
list_items = $('li.random_background_color');
var numberOfBoxes = list_items.length;

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
//For Loop:

var randomColors = [];
var counter = 0
for (var i = 1; i <= numberOfBoxes * 5; i++) {
    var randomColor = new RColor;
    counter += 1
    randomColors[i] = randomColor.get(true);
}

$(".srbc").children().children(".random_background_color").addClass("set_random_background_color");
$(".srhbc").children("a").children(".random_hover_border_color").addClass("set_random_hover_border_color");
$(".srhbc-b").children("a").children(".random_hover_border_color_bottom").addClass("set_random_hover_border_color_bottom");
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
//2nd For Loop:

var counter = 0;
$('.set_random_background_color').css("background-color", function () {
    counter += 1;
    return randomColors[counter];
});

var ul_bg_color = $('.srbc').css( "background-color" );


var counter2 = numberOfBoxes;
$('.set_random_background_color').hover(function(){
    $(this).css({'background-color': ul_bg_color});
 }, function(){
        $(this).css("background-color", function () {
            counter2 += Math.floor((Math.random()*3)+1);   
            if (counter2 > numberOfBoxes * 3) {
                counter2 = (numberOfBoxes);
            };
    return randomColors[counter2];
    });
});



var counter3 = numberOfBoxes * 3;
$('.set_random_hover_border_color').hover(function(){
    $(this).css("border", function(){

        if (counter3 > (numberOfBoxes * 5)-1) {
            counter3 = (numberOfBoxes * 3);
        }
        counter3 += 1;
        return "solid 5px " + randomColors[counter3];
    });
},  function(){
    $(this).css({'border':'5px solid white'});
} );

// Bottom border:

var counter4 = numberOfBoxes * 3;
$('.set_random_hover_border_color_bottom').hover(function(){
    $(this).css("border", function(){

        if (counter4 > (numberOfBoxes * 5)-1) {
            counter4 = (numberOfBoxes * 3);
        }
        counter4 += 1;
        return "solid 2px " + randomColors[counter4];
    });
},  function(){
    $(this).css({'border':'2px solid white'});
} );


//===========================================================================
//===========================================================================

//REVERSE!!

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
//Count Boxes:
var hover_list_items = []
hover_list_items = $('li.hover_random_background_color');
var hoverNumberOfBoxes = hover_list_items.length;

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
//For Loop:

var hoverRandomColors = [];
var hover_counter = 0
for (var i = 1; i <= hoverNumberOfBoxes * 3; i++) {
    var hoverRandomColor = new RColor;
    hover_counter += 1
    hoverRandomColors[i] = hoverRandomColor.get(true);
}

$("ul.hsrbc").children("a").children("li.hover_random_background_color").addClass("hover_set_random_background_color");
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
//2nd For Loop:

var hover_ul_bg_color = $('.hsrbc').css( "background-color" );


var hover_counter2 = 0;
$('.hover_set_random_background_color').hover(function(){
    $(this).css("background-color", function () {
        if (hover_counter2 > (hoverNumberOfBoxes * 3)-1) {
            hover_counter2 = 0;
        };
        hover_counter2 += 1;
        return hoverRandomColors[hover_counter2];
    });
}, function(){
    $(this).css({'background-color': hover_ul_bg_color});
});

//===========================================================================
//===========================================================================

//Static Background color:

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
//Count Boxes:
var static_list_items = []
static_list_items = $('.static_random_background_color');
var staticNumberOfBoxes = static_list_items.length;

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
//For Loop:

var staticRandomColors = [];
var static_counter = 0
for (var i = 1; i <= staticNumberOfBoxes * 3; i++) {
    var staticRandomColor = new RColor;
    static_counter += 1
    staticRandomColors[i] = staticRandomColor.get(true);
}

$(".strbc").children(".static_random_background_color").addClass("static_set_random_background_color");
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
//2nd For Loop:
var static_counter2 = 0;
$('.static_set_random_background_color').css("background-color", function () {
    static_counter2 += 1;
    return staticRandomColors[static_counter2];
});

$( ".static_random_background_color" ).append( staticRandomColors[0] );

} );


