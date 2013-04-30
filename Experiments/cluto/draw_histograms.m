function [] =draw_histograms(data)
   figure
    noc=size(unique(data(:,2)),1);
    for i=1:noc,
        temp=data(data(:,2)==i-1);
        subplot(2,5,i);
        [N,binCenters]=hist(temp,2);
        
       
        hBar = bar(binCenters,N,'hist');  %# Plot the histogram
        index = binCenters<0.5;  %# Find the index of the
                                                 %#   bin containing 0.7
        colors = [index(:) ...               %# Create a matrix of RGB colors to make
          zeros(numel(index),1) ...  %#   the indexed bin red and the other bins
          0.5.*(~index(:))];         %#   dark blue
        set(hBar,'FaceVertexCData',colors);  %# Re-color the bins
        title(strcat('Cluster ',char(48+i-1)))
       
  end
   
end
