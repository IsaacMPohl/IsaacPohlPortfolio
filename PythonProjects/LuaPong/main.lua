push = require 'push' --import class
Class = require 'class'
require 'Ball'
require 'Paddle'

--physical window
WINDOW_WIDTH=1290
WINDOW_HEIGHT=720
--viratual width size: Your coordinates will be based on this system
VIRTUAL_WIDTH=432
VIRTUAL_HEIGHT=243

PADDLE_SPEED1 = 200
PADDLE_SPEED2 = 200
PADDLE_SPEED3 = 200
PADDLE_SPEED4 = 200 

scoreInRow = 0
--RUNS WHEN THE GAME FIRST STARTS UP, only once... only once
function love.load()

    
    --nearest - nearest filtering on upcaling and downscaling to prevent blurring of text and graphics
    love.graphics.setDefaultFilter('nearest', 'nearest')
    
    --set the title of the window
    love.window.setTitle('Pong')

    --set the seed or the "randomess" of the serve
    -- if we set the "randomess" based, on time, int theory it is themost random
    math.randomseed(os.time())


    --more retro looking font we need to load it in newFont('file,size')
    smallFont= love.graphics.newFont('font.ttf',8)
    scoreFont= love.graphics.newFont('font.ttf',30)
    largeFont= love.graphics.newFont('font.ttf',16)
    -- set the font to the retro look
    love.graphics.setFont(smallFont)

    sounds = {
        ['paddle_hit'] = love.audio.newSource('sounds/paddle_hit.wav', 'static'),
        ['score']= love.audio.newSource('sounds/score.wav', 'static'),
      }
    --initialize our virtual res screen inside of the origional window size
    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
        fullscreen=false,
        resizable=false,
        vsync=true
    })
    --set up the paddle location
    player1Score=7
    player2Score=7
    player3Score=7
    player4Score=7

    --create a Paddle
    player1= Paddle(10,30,5,20)
    player2= Paddle(VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT-30,5,20)
    player3= Paddle(VIRTUAL_WIDTH/2,VIRTUAL_HEIGHT-10,20,5)
    player4= Paddle(VIRTUAL_WIDTH/2,5,20,5)
    --create a ball
    --      Constructor(x,y,w,h)
    ball = Ball(VIRTUAL_WIDTH/2-2,VIRTUAL_HEIGHT/2-2,4,4)
    serving = (math.random(0,3)+1)
    if serving == 1 then
        servingPlayer = 1 
        player1.y = VIRTUAL_HEIGHT/2
        ball:reset1(player1)
    elseif serving == 2 then
        servingPlayer = 2
        player2.y = VIRTUAL_HEIGHT/2
        ball:reset2(player2)
    elseif serving == 3 then
        servingPlayer = 3
        player3.x = VIRTUAL_WIDTH/2
        ball:reset3(player3)
    elseif serving == 4 then
        servingPlayer = 4
        player4.x = VIRTUAL_WIDTH/2
        ball:reset4(player4)
    end

    --seting up the game to be in a "startmode" or "main menu"
    gameState = 'start'

end

--update runs every time the screen refreshes
function love.update(dt)      
    --player 1 or left sid"""e movement (the variable)
    if love.keyboard.isDown('w') then
        player1.dy=-PADDLE_SPEED1
        print(dt)

        
    elseif love.keyboard.isDown('s') then
        player1.dy=PADDLE_SPEED1
    else
        player1.dy=0
    print(dt)

    end
    --player 2 or right side movement
    if love.keyboard.isDown('up') then
        player2.dy=-PADDLE_SPEED2

    elseif love.keyboard.isDown('down') then
        player2.dy=PADDLE_SPEED2
    else
        player2.dy=0
    print(dt)
    end
 

     --player 3 or right side movement
     if love.keyboard.isDown('n') then
        player3.dx=-PADDLE_SPEED3
     
     elseif love.keyboard.isDown('m') then
        player3.dx=PADDLE_SPEED3
     else
        player3.dx=0
     
     end
     --player 4 or up side movement
     if love.keyboard.isDown('z') then
        player4.dx=-PADDLE_SPEED4
     
     elseif love.keyboard.isDown('x') then
        player4.dx=PADDLE_SPEED4
     else
        player4.dx=0
        print(dt)

     end

    if gameState == 'serve' then
        --before swichting to play, set the ball's velocity
        if servingPlayer == 1 or servingPlayer==2 then
            if servingPlayer ==1 then
                player1.y = VIRTUAL_HEIGHT/2
                ball.dx = math.random(160,180)
                
                
            elseif servingPlayer ==2 then
                player2.y = VIRTUAL_HEIGHT/2
             
                ball.dx = -math.random(160,180)
            ball.dy=math.random(-30,30)

            end
        end
        if servingPlayer == 3 or servingPlayer==4 then
            if servingPlayer ==3 then
                player3.x = VIRTUAL_WIDTH/2
               
                ball.dy = -math.random(160,180)
            elseif servingPlayer ==4 then
                player4.x =     VIRTUAL_WIDTH/2
             
                ball.dy = math.random(160,180)
            ball.dx=math.random(-50,50)
            end
        end

    elseif gameState=='play' then
        if ball:collides(player1) then
            ball.dx = -ball.dx *1.03 --1.03 to speed up
            ball.x = player1.x+5  --to move the ball off the paddle

            --reset the y velocity
            if ball.dy<0 then
                ball.dy =  -math.random(10,150)
                
            else
                ball.dy = math.random(10,150)
                
            end
        end

        if ball:collides(player2) then
            ball.dx = -ball.dx *1.03 --1.03 to speed up
            ball.x = player2.x-5  --to move the ball off the paddle

            --reset the y velocity
            if ball.dy<0 then
                ball.dy =  -math.random(10,150)
            else
                ball.dy = math.random(10,150)
            end
            sounds['paddle_hit']:play()
        end
        if ball:collides(player3) then
            ball.dy = -ball.dy *1.03 --1.03 to speed up
            ball.y = player3.y-5  --to move the ball off the paddle

            --reset the y velocity
            if ball.dx<0 then
                ball.dx = - math.random(10,150)
            else
                ball.dx = math.random(10,150)
            end
            sounds['paddle_hit']:play()
        end
        if ball:collides(player4) then
            ball.dy = -ball.dy *1.03 --1.03 to speed up
            ball.y = player4.y+5  --to move the ball off the paddle

            --reset the y velocity
            if ball.dx<0 then
                ball.dx =  -math.random(10,150)
            else
                ball.dx = math.random(10,150)
            end
            sounds['paddle_hit']:play()
        end

        --wall collidion
        -- if ball.y<0 then 
        --     ball.y=0
        --     ball.dy=-ball.dy
        --     sounds['wall_hit']:play()
        -- end
        -- if ball.y>= VIRTUAL_HEIGHT-4 then
            -- ball.y = VIRTUAL_HEIGHT-4
            -- ball.y = VIRTUAL_HEIGHT-4
            -- ball.dy = - ball.dy
            -- sounds['wall_hit']:play()
        -- end

        ball:update(dt)
    end
    --if the ball reaches the left edge of the screen, 
    -- reset the ball and update the score
    if ball.x<0 then 
        if servingPlayer == player1 then
            scoreInRow = scoreInRow + 1 
        else 
            scoreInRow = 0 
        end
        if scoreInRow == 3 then
            PADDLE_SPEED1=300
        end

        player1Score =player1Score-1
        servingPlayer = 1
        player1.y = VIRTUAL_HEIGHT/2
        ball:reset1(player1)
        if player1Score <= 0 then 
            losingPlayer =1
            gameState='done'
        else
            gameState='serve' 
        end
       
 
    --if the ball reaches the right edge of the screen,
    --reset the ball and update the score
    elseif ball.x>VIRTUAL_WIDTH then
        if servingPlayer == player2 then
            scoreInRow = scoreInRow + 1 
        else 
            scoreInRow = 0 
        end
        if scoreInRow == 3 then
            PADDLE_SPEED2=300
        end

        player2Score =player2Score-1
        servingPlayer = 2
        player2.y = VIRTUAL_HEIGHT/2
        ball:reset2(player2)

        if player2Score <= 0 then 
            losingPlayer =2
            gameState='done'
        else
            gameState='serve'
        end
        sounds['score']:play()
       

    elseif ball.y>VIRTUAL_HEIGHT then
        if servingPlayer == player3 then
            scoreInRow = scoreInRow + 1 
        else 
            scoreInRow = 0 
        end
        if scoreInRow == 3 then
            PADDLE_SPEED3=300
        end
        player3.x = VIRTUAL_WIDTH/2
        ball:reset3(player3)
        player3Score =player3Score-1
        servingPlayer = 3
        if player3Score <= 0 then 
            losingPlayer =3 
            gameState='done'
        else
            gameState='serve'
        end
        sounds['score']:play()
       
    elseif ball.y<0 then
        if servingPlayer == player4 then
            scoreInRow = scoreInRow + 1 
        else 
            scoreInRow = 0 
        end
        player4.x = VIRTUAL_WIDTH/2
        ball:reset4(player4)
        if scoreInRow == 3 then
            PADDLE_SPEED4=300
        end
        player4Score =player4Score-1
        servingPlayer = 4
        if player4Score <= 0 then 
            losingPlayer =4 
            gameState='done'
        else
            gameState='serve'
        end
        sounds['score']:play()
     

    end
    player1:update(dt)
    player2:update(dt)
    player3:update2(dt)
    player4:update2(dt)
end

function love.keypressed(key)
    --key can be accessed by string name
    if key == 'escape' then
        love.event.quit()
    elseif key == 'enter' or key=='return'  then 
        if gameState=='start' then 
            gameState='serve'
        elseif gameState == 'serve' then
            gameState = 'play'
        elseif gameState == 'done' then
            gameState='serve'
            player1Score=7
            player2Score = 7
            player3Score=7
            player4Score=7
            PADDLE_SPEED1 = 200
            PADDLE_SPEED2 = 200
            PADDLE_SPEED3 = 200
            PADDLE_SPEED4 = 200 
            if losingPlayer == 1 then 
                servingPlayer=1 
                ball:reset1(player1)
            elseif losingPlayer == 2 then 
                servingPlayer=2
                ball:reset2(player2)
            elseif losingPlayer == 3 then 
                servingPlayer=3
                ball:reset3(player3)
            else
                servingPlayer=4
                ball:reset4(player4)
            end
            
        end
    end
end

--Called after update function by LOVe2D, this draws what is on your screen
function love.draw()


   --begin redering a virtual res
   push:apply('start')
    --clear the screen AND set the background color(R,G,B,A)
   love.graphics.clear(40,45,52,255)
   love.graphics.setFont(smallFont)
   if gameState == 'start' then
    love.graphics.setFont(smallFont)
    love.graphics.printf('Welcome to Pong!', 0, 10, VIRTUAL_WIDTH, 'center')
    love.graphics.printf('Press Enter to begin!', 0, 20, VIRTUAL_WIDTH, 'center')
    love.graphics.printf('Instructions', 0, 130, VIRTUAL_WIDTH, 'center')
    love.graphics.printf('Player 1 is Blue player (w-up) (s-down)', 0, 140, VIRTUAL_WIDTH, 'center')
    love.graphics.printf('Player 2 is Yellow player (up arrow- up) (down arrow- down)', 0, 150, VIRTUAL_WIDTH, 'center')
    love.graphics.printf('Player 3 is Green (n - left) (m- right)', 0, 160, VIRTUAL_WIDTH, 'center')
    love.graphics.printf('Player 4 is Red (z - left) (x - right)', 0, 170, VIRTUAL_WIDTH, 'center')
   


    elseif gameState == 'serve' then
        love.graphics.setFont(smallFont)
        love.graphics.printf('Player ' .. tostring(servingPlayer) .. "'s serve!", 
            0, 10, VIRTUAL_WIDTH, 'center')
        love.graphics.printf('Press Enter to serve!', 0, 20, VIRTUAL_WIDTH, 'center')
    elseif gameState == 'play' then
        -- no UI messages to display in play
    elseif gameState == 'done' then
        love.graphics.setFont(largeFont)
        love.graphics.printf('Player ' .. tostring(losingPlayer) .. ' loses!',
            0, 10, VIRTUAL_WIDTH, 'center')
        love.graphics.setFont(smallFont)
        love.graphics.printf('Press Enter to restart!', 0, 30, VIRTUAL_WIDTH, 'center')        
    end

   --printing score board
   love.graphics.push()
   love.graphics.setFont(scoreFont)

   --blue
   love.graphics.setColor(0,0,255)
   love.graphics.print(tostring(player1Score), VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 3)
   player1:render()
   --yellow
   love.graphics.setColor(255,255,0)
   love.graphics.print(tostring(player2Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3)
   player2:render()
   --green
   love.graphics.setColor(0, 255, 0)
   love.graphics.print(tostring(player3Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3-30)
   player3:render()
   --red
   love.graphics.setColor(255, 0, 0)
   love.graphics.print(tostring(player4Score), VIRTUAL_WIDTH / 2 -50, VIRTUAL_HEIGHT / 3-30)
   love.graphics.pop()
   player4:render()
   love.graphics.setColor(255,255,255)
   
   --ball 
   ball:render()
   displayFPS()

   --end rendering of virtual res
   push:apply('end')
end

function displayFPS()
    -- simple FPS display across all states
    love.graphics.setFont(smallFont)
    love.graphics.setColor(0, 255, 0, 255)
    love.graphics.print('FPS: ' .. tostring(love.timer.getFPS()), 10, 10)
end

--[[
    Called by LÖVE whenever we resize the screen; here, we just want to pass in the
    width and height to push so our virtual resolution can be resized as needed.
]]
function love.resize(w, h)
    push:resize(w, h)
end
