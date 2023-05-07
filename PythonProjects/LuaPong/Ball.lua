--class Ball
Ball = Class{}

--def __int__(self:) Constructor

function Ball:init(x,y,width,height)
    self.x = x 
    self.y = y 
    self.width = width
    self.height = height

    self.dx = math.random(2) == 1 and -100 or 100
    self.dy = math.random(-50,50) 
end

function Ball:collides(paddle)
    -- first, check to see if the left edge of either is farther to the right
    -- than the right edge of the other
    if self.x > paddle.x + paddle.width or paddle.x > self.x + self.width then
        return false
    end

    -- then check to see if the bottom edge of either is higher than the top
    -- edge of the other
    if self.y > paddle.y + paddle.height or paddle.y > self.y + self.height then
        return false
    end 

    -- if the above aren't true, they're overlapping
    return true
end

--reset the ball
function Ball:reset1(player1)
    self.x=player1.x+6
    self.y=player1.y
    --GIVEN THE BALL'S X AND Y VELOCITY A RANDOM STARTING BALUE
    -- THE AND/OR PATTERN HERE IS LU'S WAY OF ACCOMPLUSHING A TEMARY OPERATION
    -- preset the ball's velocity vector
    self.dx = math.random(2) ==1 and 100 or -100
    self.dy= math.random(-50,50) *1.5
end
function Ball:reset2(player1)
    self.x=player1.x-6
    self.y=player1.y
    --GIVEN THE BALL'S X AND Y VELOCITY A RANDOM STARTING BALUE
    -- THE AND/OR PATTERN HERE IS LU'S WAY OF ACCOMPLUSHING A TEMARY OPERATION
    -- preset the ball's velocity vector
    self.dx = math.random(2) ==1 and 100 or -100
    self.dy= math.random(-50,50) *1.5
end
function Ball:reset3(player1)
    self.x=player1.x
    self.y=player1.y-6
    --GIVEN THE BALL'S X AND Y VELOCITY A RANDOM STARTING BALUE
    -- THE AND/OR PATTERN HERE IS LU'S WAY OF ACCOMPLUSHING A TEMARY OPERATION
    -- preset the ball's velocity vector
    self.dx = math.random(2) ==1 and 100 or -100
    self.dy= math.random(-50,50) *1.5
end
function Ball:reset4(player1)
    self.x=player1.x
    self.y=player1.y+6
    --GIVEN THE BALL'S X AND Y VELOCITY A RANDOM STARTING BALUE
    -- THE AND/OR PATTERN HERE IS LU'S WAY OF ACCOMPLUSHING A TEMARY OPERATION
    -- preset the ball's velocity vector
    self.dx = math.random(2) ==1 and 100 or -100
    self.dy= math.random(-50,50) *1.5
end
--update the ball
function Ball:update(dt)
    self.x = self.x+self.dx*dt
    self.y = self.y+self.dy*dt

end

--draw the ball on the screen
function Ball:render()
   love.graphics.rectangle('fill',self.x,self.y,self.width,self.height)

end