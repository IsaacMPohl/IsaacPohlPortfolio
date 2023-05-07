-- class Paddle

Paddle = Class{}

-- def __init__(self):  Constructor
function Paddle:init(x,y,width,height)
     self.x = x
     self.y = y
     self.width = width
     self.height = height
     self.dy=0
end

--update the Paddle
function Paddle:update(dt)
     --change class to dx value for four player ????
     if self.dy<0 then
          self.y = math.max(0, self.y + self.dy *dt)
     else
          self.y = math.min(VIRTUAL_HEIGHT-self.height,self.y +self.dy*dt)
     end
     
end
function Paddle:update2(dt)
     if self.dx<0 then
          self.x = math.max(0, self.x + self.dx *dt)
     else
          self.x = math.min(VIRTUAL_WIDTH-self.width,self.x +self.dx*dt)
     end
     
end

--draw the Paddle onto the screen
function Paddle:render()
     love.graphics.rectangle('fill',self.x,self.y,self.width,self.height) 
end