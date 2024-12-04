// Lista de episódios com informações
const episodes = [
    { title: 'EP 01 - EMPREGABILIDADE', link: '#', description: 'Falamos da empregabilidade e tendências do mercado de tecnologia, com', speaker: 'Luana Alves', image: './Assets/img/ep1.svg', audio: './Assets/audio/audio.mp3' },
    { title: 'EP 02 - INGLÊS', link: '#', description: 'Falamos da importância do inglês para o mercado de tecnologia, com', speaker: 'João Silva', image: './Assets/img/ep2.svg', audio: './Assets/audio/audio2.mp3' },
    { title: 'EP 03 - DIA-A-DIA NO LAB', link: '#', description: 'Sobre como é o dia-a-dia no Lab de inovação, com', speaker: 'Leonardo Martins', image: './Assets/img/ep3.svg', audio: './Assets/audio/audio3.mp3' },
    { title: 'EP 04 - EQUIPE MANGUETOWN', link: '#', description: 'Falamos sobre a criação de um projeto que une tecnologia e cultura, com', speaker: 'MangueTown', image: './Assets/img/ep4.svg', audio: './Assets/audio/audio4.mp3' },
    { title: 'EP 05 - ESTUDANTE EMBARQUE', link: '#', description: 'Falamos sobre o processo e estudo no programa Embarque Digital, com', speaker: 'Felipe', image: './Assets/img/ep5.svg', audio: './Assets/audio/audio5.mp3' },
];

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
                        <p>${episode.description} <u>${episode.speaker}</u></p>
                    </div>
                </div>
            </div>
        </div>
    `;
    return box;
}

// Inicialização dinâmica
document.addEventListener('DOMContentLoaded', function () {
    // Seleção das colunas
    const upColumn = document.querySelector('.up-column');
    const midColumn = document.querySelector('.mid-column');
    const dowColumn = document.querySelector('.dow-column');

    // Contadores para as colunas
    let upCount = 0;
    let midCount = 0;
    let dowCount = 0;

    episodes.forEach((episode) => {
        const box = createBox(episode);

        if (upCount < 2) {
            upColumn.appendChild(box); // Coloca as 2 primeiras boxes na upColumn
            upCount++;
        } else if (midCount < 2) {
            midColumn.appendChild(box); // Coloca até 3 boxes na midColumn
            midCount++;
        } else if (dowCount < 2) {
            dowColumn.appendChild(box); // Coloca até 2 boxes na dowColumn
            dowCount++;
        }
    });

    // Inicializa o MediaElement.js nos players de áudio
    const players = document.querySelectorAll('.mejs-player');
    players.forEach(player => {
        new MediaElementPlayer(player, {
            features: ['playpause', 'progress', 'current', 'duration', 'volume', 'fullscreen']
        });
    });
});
