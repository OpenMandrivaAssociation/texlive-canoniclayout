Name:		texlive-canoniclayout
Version:	20111101
Release:	1
Summary:	TeXLive canoniclayout package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/canoniclayout.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/canoniclayout.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/canoniclayout.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive canoniclayout package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
