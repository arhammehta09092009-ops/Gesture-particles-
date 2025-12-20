<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ultimate Sensor Particles + Pinch</title>
<style>
  body { margin:0; overflow:hidden; background:#000; }
  canvas { display:block; touch-action: none; } /* prevent pinch zoom default */
</style>
</head>
<body>
<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
<script>

let scene, camera, renderer, particles = [], particleCount = 500;
let colorHue = 0;
let tilt = {x:0, y:0};
let pinch = {active:false, x:0, y:0};

// Initialize Three.js
function init(){
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
    camera.position.z = 60;

    renderer = new THREE.WebGLRenderer({antialias:true});
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    const geometry = new THREE.SphereGeometry(0.7, 8, 8);

    for(let i=0; i<particleCount; i++){
        let material = new THREE.MeshBasicMaterial({color: new THREE.Color(`hsl(${Math.random()*360},100%,50%)`)});
        let p = new THREE.Mesh(geometry, material);
        p.position.set((Math.random()-0.5)*100, (Math.random()-0.5)*100, (Math.random()-0.5)*100);
        p.velocity = new THREE.Vector3();
        scene.add(p);
        particles.push(p);
    }

    animate();
}

// Tilt (gravity-like)
window.addEventListener('deviceorientation', (e)=>{
    tilt.y = THREE.MathUtils.degToRad(e.gamma || 0)/2;
    tilt.x = THREE.MathUtils.degToRad(e.beta || 0)/2;
});

// Shake detection
let lastAccel = {x:null, y:null, z:null}, shakeThreshold = 15;
window.addEventListener('devicemotion', (e)=>{
    let a = e.accelerationIncludingGravity;
    if(lastAccel.x !== null){
        let delta = Math.abs(a.x-lastAccel.x) + Math.abs(a.y-lastAccel.y) + Math.abs(a.z-lastAccel.z);
        if(delta > shakeThreshold) explodeParticles();
    }
    lastAccel = {x:a.x, y:a.y, z:a.z};
});

// Tap to color-shift
window.addEventListener('touchstart', (e)=>{
    colorHue = (colorHue+60)%360;
    particles.forEach(p => p.material.color.setHSL(Math.random(),1,0.5));
});

// Pinch detection
let ongoingTouches = [];
function copyTouch(touch){ return {identifier: touch.identifier, pageX: touch.pageX, pageY: touch.pageY}; }

function handleStart(evt){
    evt.preventDefault();
    for(let t of evt.changedTouches) ongoingTouches.push(copyTouch(t));
    if(ongoingTouches.length === 2){
        pinch.active = true;
        pinch.x = (ongoingTouches[0].pageX + ongoingTouches[1].pageX)/2;
        pinch.y = (ongoingTouches[0].pageY + ongoingTouches[1].pageY)/2;
    }
}
function handleMove(evt){
    evt.preventDefault();
    for(let t of evt.changedTouches){
        let idx = ongoingTouches.findIndex(ot => ot.identifier === t.identifier);
        if(idx>=0) ongoingTouches[idx] = copyTouch(t);
    }
    if(ongoingTouches.length === 2){
        pinch.x = (ongoingTouches[0].pageX + ongoingTouches[1].pageX)/2;
        pinch.y = (ongoingTouches[0].pageY + ongoingTouches[1].pageY)/2;
    }
}
function handleEnd(evt){
    evt.preventDefault();
    for(let t of evt.changedTouches){
        let idx = ongoingTouches.findIndex(ot => ot.identifier === t.identifier);
        if(idx>=0) ongoingTouches.splice(idx,1);
    }
    if(ongoingTouches.length < 2) pinch.active = false;
}

document.addEventListener("touchstart", handleStart, false);
document.addEventListener("touchmove", handleMove, false);
document.addEventListener("touchend", handleEnd, false);
document.addEventListener("touchcancel", handleEnd, false);

// Explosion
function explodeParticles(){
    particles.forEach(p => {
        let angle = Math.random()*Math.PI*2;
        let speed = 5 + Math.random()*5;
        p.velocity.x = Math.cos(angle)*speed;
        p.velocity.y = Math.sin(angle)*speed;
        p.velocity.z = (Math.random()-0.5)*speed;
    });
}

// Animate
function animate(){
    requestAnimationFrame(animate);

    colorHue += 0.2;

    particles.forEach(p=>{
        // Tilt attraction
        p.position.x += tilt.y * 0.3;
        p.position.y += tilt.x * 0.3;

        // Pinch telekinesis
        if(pinch.active){
            let nx = (pinch.x/window.innerWidth - 0.5)*100;
            let ny = -(pinch.y/window.innerHeight - 0.5)*100;
            let dir = new THREE.Vector3(nx - p.position.x, ny - p.position.y, -p.position.z);
            dir.multiplyScalar(0.02);
            p.velocity.add(dir);
        }

        // Add velocity (explosion effect)
        p.position.add(p.velocity);
        p.velocity.multiplyScalar(0.92); // damping

        // Rotation & shimmer
        p.rotation.x += 0.01;
        p.rotation.y += 0.01;
        let scale = 1 + 0.3*Math.sin(Date.now()*0.005 + p.position.x);
        p.scale.set(scale, scale, scale);

        // Rainbow cycling
        let h = (colorHue + p.position.x)%360;
        p.material.color.setHSL(h/360,1,0.5);
    });

    renderer.render(scene, camera);
}

// Resize
window.addEventListener('resize', ()=>{
    camera.aspect = window.innerWidth/window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

init();

</script>
</body>
</html>
