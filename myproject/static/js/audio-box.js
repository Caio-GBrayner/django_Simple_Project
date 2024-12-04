document.addEventListener("DOMContentLoaded", function () {
    const audio = document.getElementById("audio-player");
    const playPauseBtn = document.getElementById("play-pause");
    const progressBar = document.getElementById("progress-bar");
    const volumeControl = document.getElementById("volume-control");
    const backwardBtn = document.getElementById("backward");
    const forwardBtn = document.getElementById("forward");
    const rewardBtn = document.getElementById("reward-music");
    const nextBtn = document.getElementById("next-music");
    const volumeIcon = document.getElementById("volume-icon"); // Novo botão de volume
  
    const skipTime = 10; // Tempo para avançar ou retroceder (em segundos)
  
    // Play/Pause Toggle
    playPauseBtn.addEventListener("click", () => {
      if (audio.paused) {
        audio.play();
        playPauseBtn.innerHTML = '<i class="bi bi-pause"></i>';
      } else {
        audio.pause();
        playPauseBtn.innerHTML = '<i class="bi bi-play"></i>';
      }
    });
  
    // Atualizar barra de progresso
    audio.addEventListener("timeupdate", () => {
      progressBar.value = (audio.currentTime / audio.duration) * 100;
    });
  
    // Alterar posição do áudio ao arrastar a barra de progresso
    progressBar.addEventListener("input", () => {
      audio.currentTime = (progressBar.value / 100) * audio.duration;
    });
  
    // Controle de volume
    volumeControl.addEventListener("input", () => {
      const volume = volumeControl.value / 100;
      audio.volume = volume;
  
      if (volume === 0) {
        volumeIcon.innerHTML = '<i class="bi bi-volume-mute"></i>';
      } else {
        volumeIcon.innerHTML = '<i class="bi bi-volume-up"></i>';
      }
    });
  
    // Alternar entre mute e unmute ao clicar no ícone de volume
    volumeIcon.addEventListener("click", () => {
      if (audio.volume > 0) {
        audio.volume = 0;
        volumeControl.value = 0;
        volumeIcon.innerHTML = '<i class="bi bi-volume-mute"></i>';
      } else {
        audio.volume = 1; // Define volume máximo
        volumeControl.value = 100;
        volumeIcon.innerHTML = '<i class="bi bi-volume-up"></i>';
      }
    });
  
    // Retroceder 10 segundos
    backwardBtn.addEventListener("click", () => {
      audio.currentTime = Math.max(0, audio.currentTime - skipTime);
    });
  
    // Avançar 10 segundos
    forwardBtn.addEventListener("click", () => {
      audio.currentTime = Math.min(audio.duration, audio.currentTime + skipTime);
    });
  
    // Retroceder música (início ou anterior)
    rewardBtn.addEventListener("click", () => {
      if (audio.currentTime > 5) {
        audio.currentTime = 0;
      } else {
        alert("Aqui seria implementada a lógica de música anterior.");
      }
    });
  
    // Avançar para a próxima música
    nextBtn.addEventListener("click", () => {
      alert("Aqui seria implementada a lógica para a próxima música.");
    });
  });
  