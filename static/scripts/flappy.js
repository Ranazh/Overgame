
var cvs = document.getElementById("canvas");
var ctx = cvs.getContext("2d");

var fish = new Image();
var bg = new Image();
var fg = new Image();
var rockUp = new Image();
var rockBottom = new Image();

fish.src = "{%static 'images/fish.png' %}";
bg.src = "images/background.png";
fg.src = "images/frontground.jpg";
rockUp.src = "images/rockUp.png";
rockBottom.src = "images/rockBottom.png";

var gap = 145;

// При нажатии на какую-либо кнопку
document.addEventListener("keydown", moveUp);

function moveUp(){
  yPos -= 25;
}

// Создание блоков
var rock = [];

rock[0] = {
  x : cvs.width,
  y : 0
}

var score = 0;
// Позиция рыбки
var xPos = 10;
var yPos = 150;
var grav = 1.5;

function  draw() {
  ctx.drawImage(bg, 0, 0);

  for(var i = 0; i < rock.length; i++){
      ctx.drawImage(rockUp, rock[i].x, rock[i].y);
      ctx.drawImage(rockBottom, rock[i].x, rock[i].y + rockUp.height + gap);

      rock[i].x--;

      if(rock[i].x == 70){
        rock.push({
          x : cvs.width,
          y : Math.floor(Math.random() * rockUp.height) - rockUp.height
        });
      }
      // Отслеживание сталкиваний
      if(xPos + fish.width - 50 >= rock[i].x
        && xPos <= rock[i].x + rockUp.width - 72
        && (yPos <= rock[i].y + rockUp.height
          || yPos + fish.height >= rock[i].y + rockUp.height + gap)
        || yPos + fish.height >= cvs.height - fg.height) {
            location.reload(); // Перезагрузка страницы
          }

      if(rock[i].x == 5){
        score++;
      }
  }


  ctx.drawImage(fg, 0, cvs.height - fg.height);
  ctx.drawImage(fish, xPos, yPos);

  yPos += grav;

  ctx.fillStyle = "pink";
  ctx.font = "24px Verdana";
  ctx.fillText("Score: " + score, 10, cvs.height - 20);

  requestAnimationFrame(draw);
}

rockBottom.onload = draw;

