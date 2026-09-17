/**
 * Linear map of the plane.
 *
 *     ::: {.widget src="widgets/linear-map.js" matrix="2,1,0,1"}
 *     ::: {.print}
 *     ...static figure or description for the PDF...
 *     :::
 *     :::
 *
 * Shows the unit square and its image under the matrix [[a, b], [c, d]] (given row by
 * row). Drag the images of e1 and e2 to change the matrix. Options:
 *   matrix="a,b,c,d"       initial matrix (default: identity)
 *   extent="3"             half-width of the visible square
 *   determinant="false"    hide the determinant (the signed area of the image), e.g. in
 *                          chapters before determinants are introduced
 */

function parseMatrix(text) {
    const values = (text || '1,0,0,1').split(',').map(Number);
    return values.length === 4 && values.every(Number.isFinite) ? values : [1, 0, 0, 1];
}

const round = v => Math.round(v * 100) / 100;

export default async function mount(element, options, { loadJSXGraph, ensureId, COLORS }) {
    const JXG = await loadJSXGraph();
    const [a, b, c, d] = parseMatrix(options.matrix);
    const extent = Number(options.extent) || 3;

    const boardElement = document.createElement('div');
    boardElement.className = 'widget-board';
    const readout = document.createElement('div');
    readout.className = 'widget-readout';
    element.append(boardElement, readout);

    const board = JXG.JSXGraph.initBoard(ensureId(boardElement), {
        boundingbox: [-extent, extent, extent, -extent],
        axis: true, keepAspectRatio: true, showCopyright: false, showNavigation: false,
        pan: { enabled: false }, zoom: { enabled: false },
    });

    // Unit square, faint
    board.create('polygon', [[0, 0], [1, 0], [1, 1], [0, 1]], {
        fillColor: '#999', fillOpacity: 0.1, borders: { strokeColor: '#999', dash: 2 }, vertices: { visible: false },
        fixed: true, highlight: false,
    });

    // Images of the standard basis vectors: the columns (a, c) and (b, d)
    const snap = { snapToGrid: true, snapSizeX: 0.25, snapSizeY: 0.25 };
    const e1 = board.create('point', [a, c], { name: 'Te₁', color: COLORS[0], size: 4, ...snap });
    const e2 = board.create('point', [b, d], { name: 'Te₂', color: COLORS[1], size: 4, ...snap });
    const origin = [0, 0];
    board.create('arrow', [origin, e1], { strokeColor: COLORS[0], strokeWidth: 3, fixed: true });
    board.create('arrow', [origin, e2], { strokeColor: COLORS[1], strokeWidth: 3, fixed: true });
    const corner = board.create('point', [() => e1.X() + e2.X(), () => e1.Y() + e2.Y()], { visible: false });
    board.create('polygon', [origin, e1, corner, e2], {
        fillColor: COLORS[2], fillOpacity: 0.2, borders: { strokeColor: COLORS[2] }, vertices: { visible: false },
        highlight: false, hasInnerPoints: false,
    });

    const showDeterminant = options.determinant !== 'false';
    const update = () => {
        const [m11, m21, m12, m22] = [e1.X(), e1.Y(), e2.X(), e2.Y()].map(round);
        let text = `A = [[${m11}, ${m12}], [${m21}, ${m22}]]`;
        if (showDeterminant) text += `   det A = ${round(m11 * m22 - m12 * m21)}`;
        readout.textContent = text;
    };
    board.on('update', update);
    update();
}
