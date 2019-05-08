function menu(selector) {
	let menu = $(selector);
	let button = menu.find('.menu-btn');
	let links = menu.find('.menu-link');
	let overlay = menu.find('.menu-overlay');


	button.on('click', (e) => {
		e.preventDefault();
		toggleMenu();
	});

	links.on('click', () => toggleMenu());
	overlay.on('click', () => toggleMenu());

	function toggleMenu() {
		menu.toggleClass('menu-active');

		if (menu.hasClass('menu-active')) {
			$('body').css('overflow', 'hidden');
		} else {
			$('body').css('overflow', 'visible');
		}
	}
}
menu('.menu');




function slider(selector){
	let slider = $(selector);
	let imgs = slider.children();

	slider
		.addClass('slider')
		.append('<a href="#" class="slider__arrow slider__arrow_left"></a>')
		.append('<div class="slider__slides"></div>')
		.append('<div class="slider__dots"></div>')
		.append('<a href="#" class="slider__arrow slider__arrow_right"></a>')
		.on('click', '.slider__arrow, .slider__dot', function (e) {
			e.preventDefault();

			let a = $(this);
			let active = slider.find('.slider__slide_active');
			let current = active.index();
			let next = current;
			let left = false;

			if (a.hasClass('slider__arrow_left')) {
				next = current - 1 >= 0 ? current - 1 : imgs.length -1;
				left = true;
			} else if (a.hasClass('slider__arrow_right')) {
				next = (current + 1) % imgs.length;
			} else {
				next = a.index()
				left = next < current ? true : false;
			}


			if (current == next) {
				return;
			}

			slider.append('<div class="slider__temp"></div>');

			let temp = slider.find('.slider__temp');
			let i = current;
			let j = 0;
			let animate = {};

			while (true) {
				let img = imgs
					.eq(i)
					.clone()
					.css({
						display: 'inline-block',
						width: slider.css('width')
					});

				if (left) {
					img.prependTo(temp);
				} else {
					img.appendTo(temp);
				}

				if (i == next) {
					break;
				}

				if (left) {
					i = i - 1 >= 0 ? i - 1 : imgs.length -1;
					j--;
				} else {
					i = (i + 1) % imgs.length;
					j++;
				}
			}

			temp.css({
				width: (Math.abs(j) +1) * 100 + '%',
				position: 'absolute',
				top: 0
			});

			if (left) {
				temp.css('left', j * 100 + '%');
				animate.left =0;
			} else {
				temp.css('left', 0);
				animate.left = j* -100 + '%';
			}

			active.removeClass('slider__slide_active');
			slider
				.find('.slider__dot_active')
				.removeClass('slider__dot_active');

			imgs
				.eq(next)
				.addClass('slider__slide_active');
			slider
				.find('.slider__dot')
				.eq(next)
				.addClass('slider__dot_active')


			temp.animate(animate, 500, function () {
				temp.remove();
			})
		});

	let slides = slider.children('.slider__slides');
	let dots = slider.children('.slider__dots');

	imgs
		.prependTo(slides)
		.each(function (i){

			if(!i) {
				dots.append('<a href="#" class="slider__dot slider__dot_active"></a>');
			} else {
				dots.append('<a href="#" class="slider__dot"></a>');
			}
		})
		.addClass('slider__slide')
		.eq(0)
		.addClass('slider__slide_active')


}


slider('#slider')




// ScrollToTop

var html, body, scrollToTopButton;
window.onload = function() {
  html = document.documentElement;
  body = document.body;
  scrollToTopButton = document.getElementById("scrollToTopButton");
};

function scrollToTop(totalTime, easingPower) {
  //console.log("here");
  var timeInterval = 1; //in ms
  var scrollTop = Math.round(body.scrollTop || html.scrollTop);
  //var by=- scrollTop;
  var timeLeft = totalTime;
  var scrollByPixel = setInterval(function() {
    var percentSpent = (totalTime - timeLeft) / totalTime;
    if (timeLeft >= 0) {
      var newScrollTop = scrollTop * (1 - easeInOut(percentSpent, easingPower));
      body.scrollTop = newScrollTop;
      html.scrollTop = newScrollTop;
      //console.log(easeInOut(percentSpent,easingPower));
      timeLeft--;
    } else {
      clearInterval(scrollByPixel);
      //Add hash to the url after scrolling
      //window.location.hash = hash;
    }
  }, timeInterval);
}

function easeInOut(t, power) {
  if (t < 0.5) {
    return 0.5 * Math.pow(2 * t, power);
  } else {
    return 0.5 * (2 - Math.pow(2 * (1 - t), power));
  }
}

window.onscroll = controlScrollToTopButton;

function controlScrollToTopButton() {
  var windowInnerHeight = 1.5 * window.innerHeight;
  if (
    body.scrollTop > windowInnerHeight ||
    html.scrollTop > windowInnerHeight
  ) {
    scrollToTopButton.classList.add("show");
  } else {
    scrollToTopButton.classList.remove("show");
  }
}


function show(state)
	{
	document.getElementById('window').style.display = state;	
	document.getElementById('gray').style.display = state; 		
	}	