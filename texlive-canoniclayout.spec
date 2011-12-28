# revision 24523
# category Package
# catalog-ctan /macros/latex/contrib/canoniclayout
# catalog-date 2011-11-06 17:08:08 +0100
# catalog-license lppl1.3
# catalog-version 0.4
Name:		texlive-canoniclayout
Epoch:		1
Version:	0.4
Release:	1
Summary:	Create canonical page layouts with memoir
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/canoniclayout
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/canoniclayout.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/canoniclayout.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/canoniclayout.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A canonic text layout has specified relations to a circle
inscribed within the enclosing page. The package allows the
user to use a canonic layout with the memoir class.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/canoniclayout/canoniclayout.sty
%doc %{_texmfdistdir}/doc/latex/canoniclayout/README
%doc %{_texmfdistdir}/doc/latex/canoniclayout/canoniclayout.pdf
#- source
%doc %{_texmfdistdir}/source/latex/canoniclayout/canoniclayout.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
