%global tl_name canoniclayout
%global tl_revision 64889

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Create canonical page layouts with memoir
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/canoniclayout
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/canoniclayout.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/canoniclayout.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/canoniclayout.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A canonic text layout has specified relations to a circle inscribed
within the enclosing page. The package allows the user to use a canonic
layout with the memoir class.

