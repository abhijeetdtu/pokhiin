var Bot = function(bot ,p ,b, w){
	
	this.self = bot;
	this.player = p;
	this.world = w;
	this.ball = b;
	this.lastUpdate = new Date().getSeconds();
	this.currentTime = new Date();
	this.tactics = {
		initPosition:{x:this.self.state.pos.x, y:this.self.state.pos.y},
		center: this.world.renderer().width/2,
		reach : this.self.radius*10,
		errorDistance: this.self.radius,
		stepLength: this.self.radius/10,
		stepSize: 10,
		tooClose: this.self.radius + 2*this.ball.radius,
		speed:this.ball.radius,
		hitForce:10,
		destination:{x:this.self.state.pos.x, y:this.self.state.pos.y}

	}

	this.update = function(){
			this.play();
	}

	this.moveTo = function(position , speed){
		this.tactics.destination = position;
		if(this.isAtDestination()){
			this.tactics.destination = false;
			return;
		}
		var temp = Physics.vector();
		temp.clone(position);
		temp.vsub(this.self.state.pos);
		temp.normalize();
		temp.mult(speed);
		this.self.state.pos.add(temp.x , temp.y);
	}

	this.movementUpdate = function(){
		if(this.isAtDestination())
			return;
		else{
			this.moveTo(this.tactics.destination , this.tactics.speed);
		}
	}

	this.pushBall = function(force){
		console.log(force.x + " " + force.y);
		var t = this.ball;
		this.ball.applyForce(force);

	}

	this.getToDefensivePosition = function(){
		this.tactics.destination = this.tactics.initPosition;
		this.moveTo(this.tactics.destination, this.tactics.speed);
		this.tactics.destination = false;
	}

	this.attack = function(position){
		//this.push(this.getBestAttackDirection());
		
	}

	this.play = function(){
		
		this.movementUpdate();

		if(this.ball.state.pos.x < this.self.state.pos.x){
			//console.log(1);
			this.tactics.destination = {x:this.ball.state.pos.x - this.self.radius*2.5 , y:this.ball.state.pos.y}
			//this.attack(this.ball.state.pos);
		}
		else if(this.self.state.pos.x > this.world.renderer().width/2 || (this.ball.state.vel.x > 0 && this.ball.state.pos.x > this.tactics.center)){
			this.tactics.destination = this.tactics.initPosition;
		}
		else{
			if(this.ballInTouch()){
				console.log("BALL HIT");
				this.pushBall(this.getBestAttackDirection(this.tactics.hitForce));
			}
			else if(this.ballInRange()){
				//console.log(4);
				if(this.ball.state.vel.x < 0){
					this.tactics.destination = {x: this.self.state.pos.x,y:this.ball.state.pos.y};
				}
				else
					this.tactics.destination = this.ball.state.pos;
			}
			else{
				//console.log(5);
				this.tactics.destination = {x: this.tactics.initPosition.x,y:this.ball.state.pos.y};
			}
		}
	}
	this.ballInRange = function(){
		var temp = Physics.vector();
		temp.clone(this.ball.state.pos);
		if(temp.dist(this.self.state.pos) < this.tactics.reach)
			return true;
		return false;
	}

	this.ballInTouch = function(){
		var temp = Physics.vector();
		temp.clone(this.ball.state.pos);
		//console.log(Math.floor(temp.dist(this.self.state.pos) ) + " DIST :: " +  Math.floor(this.self.radius + this.ball.radius) );
		if(Math.floor(temp.dist(this.self.state.pos) ) < Math.floor(this.self.radius + this.ball.radius)) 
			return true;
		return false;
	}

	this.isAtDestination = function(){
		if(this.tactics.destination == false)
			return true;
		else{
			var temp = Physics.vector();
			temp.clone(this.tactics.destination);
			temp.vsub(this.self.state.pos);
			if(Math.abs(temp.x) < this.tactics.speed && Math.abs(temp.y) < this.tactics.speed)
				return true;
			else 
				return false;
		}
	}

	this.getBestAttackDirection = function(mag){
		var temp = Physics.vector();
		temp.x = this.world.renderer().width/2 + Math.random()*this.world.renderer().width/2;
		temp.y = this.world.renderer().height-this.player.state.pos.y;
		//console.log(temp.x + " " + temp.y);
		temp.vsub(this.self.state.pos);
		temp.x = temp.x/Math.sqrt(temp.x*temp.x + temp.y*temp.y);
		temp.y = temp.y/Math.sqrt(temp.x*temp.x + temp.y*temp.y);
		//console.log(temp.x + " " + temp.y);
		if(mag)
			temp.mult(mag);
		return temp;
	}
}; 

