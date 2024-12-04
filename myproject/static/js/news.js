// Lista de episódios com informações
const episodes = [
    { title: 'EP 03 - DIA-A-DIA NO LAB', link: '#', description: 'Sobre como é o dia-a-dia no Lab de inovação, com', speaker: 'Leonardo Martins', image: '../../Assets/img/ep3.svg', audio: '../../Assets/audio/audio.mp3' },
    { title: 'EP 04 - EQUIPE MANGUETOWN', link: '#', description: 'Falamos sobre a criação de um projeto que une tecnologia e cultura, com', speaker: 'MangueTown', image: '../../Assets/img/ep4.svg', audio: '../../Assets/audio/audio4.mp3' },
    { title: 'EP 05 - ESTUDANTE EMBARQUE', link: '#', description: 'Falamos sobre o processo e estudo no programa Embarque Digital, com', speaker: 'Felipe', image: '../../Assets/img/ep5.svg', audio: '../../Assets/audio/audio5.mp3' },
];

// Seleção da coluna onde os episódios serão inseridos
const midColumn = document.querySelector('.mid-column');

// Função para criar o HTML de cada episódio
function createBox(episode) {
    const box = document.createElement('div');
    box.classList.add('box');

    box.innerHTML = `
        <div class="box-container">
            <div class="visual-box">
                <img src="${episode.image}" alt="${episode.title}" class="box-image">
                <div class="box-content">
                    <div class="title-box">
                        <h3>${episode.title}</h3>
                        <p>${episode.description} <u>${episode.speaker}.</u></p>
                    </div>
                </div>
            </div>
            <div class="complement-box">
                <!-- Player de áudio usando MediaElement.js -->
                <div class="audio-player">
                    <audio class="mejs-player" controls>
                        <source src="${episode.audio}" type="audio/mpeg">
                    </audio>
                </div>
            </div>
        </div>
    `;
    return box;
}

document.addEventListener('DOMContentLoaded', function () {
    // Limpar a coluna "mid-column" antes de adicionar novos episódios
    midColumn.innerHTML = '';

    // Adicionar os episódios à coluna "mid-column"
    episodes.forEach((episode) => {
        const box = createBox(episode);
        midColumn.appendChild(box); // Adiciona cada episódio na mid-column
    });

    // Inicializar o MediaElement.js nos players de áudio
    const players = document.querySelectorAll('.mejs-player');
    players.forEach(player => {
        new MediaElementPlayer(player, {
            features: ['playpause', 'progress', 'current', 'duration', 'volume', 'fullscreen']
        });
    });
});
